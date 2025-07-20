# firebase_utils.py
# This file handles all the Firebase initialization and basic operations.

import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
import json
import uuid # For generating anonymous user IDs if needed

# --- IMPORTANT: Global Variables from Canvas Environment ---
# These variables are provided by the hosting environment for Firebase.
# DO NOT change their names or how they are accessed.
# For local testing, these might be None or cause StreamlitSecretNotFoundError.
# We'll use .get() with a default to handle cases where st.secrets is not fully configured locally.

# Safely get secrets, providing defaults if not found (for local development)
# In the actual Canvas environment, these will be populated.
_app_id = st.secrets.get("__app_id", "default-app-id-local") # Use a default local ID
_firebase_config_str = st.secrets.get("__firebase_config", None) # Default to None if not found
_initial_auth_token = st.secrets.get("__initial_auth_token", None) # Default to None if not found

# --- Firebase Initialization ---
# This function initializes Firebase ONLY ONCE.
def initialize_firebase():
    if not firebase_admin._apps: # Check if Firebase is already initialized
        try:
            if _firebase_config_str:
                # Firebase config is provided as a JSON string
                firebase_config = json.loads(_firebase_config_str)
                
                # Attempt to use credentials.Certificate if all necessary fields are present
                # This is for robust initialization in Canvas or if a full service account JSON is provided locally
                cred_dict = {
                    "type": firebase_config.get("type", "service_account"),
                    "project_id": firebase_config.get("project_id"),
                    "private_key_id": firebase_config.get("private_key_id"),
                    # Handle escaped newlines in private_key for proper parsing
                    "private_key": firebase_config.get("private_key", "").replace("\\n", "\n"),
                    "client_email": firebase_config.get("client_email"),
                    "client_id": firebase_config.get("client_id"),
                    "auth_uri": firebase_config.get("auth_uri"),
                    "token_uri": firebase_config.get("token_uri"),
                    "auth_provider_x509_cert_url": firebase_config.get("auth_provider_x509_cert_url"),
                    "client_x509_cert_url": firebase_config.get("client_x509_cert_url"),
                    "universe_domain": firebase_config.get("universe_domain", "googleapis.com")
                }
                
                if all(cred_dict.get(k) for k in ["private_key", "client_email", "project_id"]):
                    cred = credentials.Certificate(cred_dict)
                    firebase_admin.initialize_app(cred, {
                        'projectId': firebase_config.get('project_id')
                    })
                    st.success("Firebase initialized successfully with provided config!")
                else:
                    st.warning("Firebase config is incomplete for full initialization. Proceeding with anonymous/token auth.")
                    firebase_admin.initialize_app() # Fallback for local testing or incomplete config
            else:
                st.warning("No Firebase config string found. Initializing for anonymous authentication only.")
                firebase_admin.initialize_app() # Initialize without credentials for anonymous auth
        except Exception as e:
            st.error(f"Error during Firebase initialization: {e}")
            st.info("Attempting anonymous sign-in as fallback due to initialization error.")
            # Ensure it's initialized even if with errors, for anonymous auth to work
            if not firebase_admin._apps: # Double check if it failed to init
                firebase_admin.initialize_app()
    
    return firebase_admin.get_app()

# Initialize Firebase when the app starts
firebase_app = initialize_firebase()
db = firestore.client(firebase_app) # Get Firestore client
auth_client = auth.get_auth(firebase_app) # Get Auth client, now directly accessible

# --- Authentication Functions ---

# Function to sign in anonymously or with custom token
def sign_in_user():
    # Ensure session state variables are initialized
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

    if st.session_state.user_id and st.session_state.logged_in: # Already have a user_id from a previous session
        st.info(f"Already signed in as: {st.session_state.user_email} (ID: {st.session_state.user_id})")
        return st.session_state.user_id

    try:
        if _initial_auth_token: # Use the safely retrieved initial_auth_token
            # Use custom token provided by the Canvas environment
            user = auth_client.verify_id_token(_initial_auth_token)
            st.session_state.user_id = user['uid']
            st.session_state.logged_in = True
            st.session_state.user_email = user.get('email', 'Custom Token User')
            st.success(f"Signed in via custom token: {st.session_state.user_email} (ID: {st.session_state.user_id})")
        else:
            # Sign in anonymously if no custom token is provided (common for local dev)
            # Create a new anonymous user (Firebase Admin SDK allows this)
            anonymous_user = auth_client.create_user(uid=str(uuid.uuid4()))
            st.session_state.user_id = anonymous_user.uid
            st.session_state.logged_in = True
            st.session_state.user_email = "Anonymous"
            st.warning(f"Signed in anonymously. User ID: {st.session_state.user_id}")
            st.info("Your preferences will be saved for this session. For permanent storage, consider creating an account.")
        return st.session_state.user_id
    except Exception as e:
        st.error(f"Authentication failed: {e}")
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.user_email = None
        return None

# Function to create a user with email and password
def create_user_with_email(email, password):
    try:
        user = auth_client.create_user(email=email, password=password)
        st.success(f"User {user.email} created successfully!")
        return user.uid
    except Exception as e:
        st.error(f"Error creating user: {e}")
        return None

# Function to sign out
def sign_out_user():
    st.session_state.user_id = None
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.user_prefs = {} 
    st.success("Signed out successfully.")
USER_PREFS_COLLECTION = f"artifacts/{_app_id}/users"
def save_user_preferences(user_id, preferences):
    if not user_id:
        st.error("Cannot save preferences: User not logged in.")
        return False
    try:
        doc_ref = db.collection(USER_PREFS_COLLECTION).document(user_id).collection("preferences").document("outfit_prefs")
        doc_ref.set(preferences)
        st.success("Preferences saved successfully!")
        return True
    except Exception as e:
        st.error(f"Error saving preferences: {e}")
        return False
def load_user_preferences(user_id):
    if not user_id:
        return None
    try:
        doc_ref = db.collection(USER_PREFS_COLLECTION).document(user_id).collection("preferences").document("outfit_prefs")
        doc = doc_ref.get()
        if doc.exists:
            st.success("Preferences loaded!")
            return doc.to_dict()
        else:
            st.info("No saved preferences found for this user.")
            return None
    except Exception as e:
        st.error(f"Error loading preferences: {e}")
        return None

