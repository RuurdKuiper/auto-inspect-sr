import openai
import streamlit as st
import pandas as pd
import requests
import pymupdf4llm
import pymupdf
import re
from requests.utils import quote
import json

from utils import *
from prompts import domain_1_prompt, domain_2_prompt, domain_3_prompt, domain_4_prompt

# Load the Retraction Watch dataset
# Initialization
if 'retraction_watch_df' not in st.session_state:
    st.session_state.retraction_watch_df = pd.read_csv('retraction_watch.csv')

st.title("INSPECT-SR Tool for Randomized Control Trial Papers")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Initialize and reset session state when a new file is uploaded
if uploaded_file:
    if 'last_uploaded_file' not in st.session_state or uploaded_file != st.session_state.get('last_uploaded_file'):
        # Reset all session state variables on new file upload
        st.session_state.update({
            'last_uploaded_file': uploaded_file,
            'domain_1_response': None,
            'domain_2_response': None,
            'domain_3_response': None,
            'domain_4_response': None,
            'pdf_text': None,
            'authors': None,
            'title': None,
        })

    # Process the uploaded file only once
    if st.session_state.pdf_text is None:
        st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
        st.session_state.authors, st.session_state.title = get_authors_and_title(st.session_state.pdf_text)

    pdf_text = st.session_state.pdf_text
    authors = st.session_state.authors
    title = st.session_state.title

    # Display the extracted information
    st.write(f"**Paper Title:** {title}")
    st.write(f"**Authors:** {authors}")
    with st.expander("View Extracted PDF Text"):
        st.write(pdf_text)

    # Domain 1: Post-publication Notices
    with st.container():
        st.header("Domain 1: Inspecting Post-Publication Notices")

        if st.button("Run Domain 1 Analysis"):
            retraction_status, retraction_details = check_retraction_status(title)
            expression_of_concern = check_expression_of_concern(title)
            author_track_record, author_retractions = check_author_track_record(authors)

            with st.expander("Retraction Database Details"):
                st.write(f"**Retraction Status:** {retraction_status}")
                st.write(f"**Details:** {retraction_details}")
                st.write(f"**Expression of Concern:** {expression_of_concern}")
                st.write(f"**Author Track Record:** {author_track_record}")
                if author_retractions:
                    st.write(author_retractions)
            prompt = domain_1_prompt(
            title=title,
            authors=authors,
            retraction_status=retraction_status,
            retraction_details=retraction_details,
            expression_of_concern=expression_of_concern,
            author_track_record=author_track_record,
            author_retractions=author_retractions,
            )
            # Run domain 1 questions through ChatGPT
            st.session_state.domain_1_response = get_chatgpt_response(prompt, pdf_text)

        # Always display Domain 1 Response if it exists
        if st.session_state.domain_1_response:
            st.write("**Domain 1 Response:**")
            st.write(st.session_state.domain_1_response)

    # Domain 2: Inspecting Conduct, Governance, and Transparency
    with st.container():
        st.header("Domain 2: Inspecting Conduct, Governance, and Transparency")

        if st.button("Run Domain 2 Analysis"):
            study_json = search_clinical_trials_full(title)

            if "Error" in study_json:
                st.error(study_json["Error"])
            else:
                with st.expander("Full ClinicalTrials.gov JSON"):
                    st.json(study_json)

                st.download_button(
                    label="Download ClinicalTrials.gov JSON",
                    data=json.dumps(study_json, indent=2),
                    file_name="study.json",
                    mime="application/json"
                )

            prompt = domain_2_prompt(title=title, authors=authors, study_json=study_json)
            st.session_state.domain_2_response = get_chatgpt_response(prompt, pdf_text)

        # Always display Domain 2 Response if it exists
        if st.session_state.domain_2_response:
            st.write("**Domain 2 Response:**")
            st.write(st.session_state.domain_2_response)

    # Domain 3: Inspecting text and figures
    with st.container():
        st.header("Domain 3: Inspecting text and figures")

        if st.button("Run Domain 3 Analysis"):

            prompt = domain_3_prompt(title=title, authors=authors)
            st.session_state.domain_3_response = get_chatgpt_response(prompt, pdf_text)

        # Always display Domain 3 Response if it exists
        if st.session_state.domain_3_response:
            st.write("**Domain 3 Response:**")
            st.write(st.session_state.domain_3_response)

    # Domain 4: Inspecting Conduct, Governance, and Transparency
    with st.container():
        st.header("Domain 4: Inspecting Conduct, Governance, and Transparency")

        if st.button("Run Domain 4 Analysis"):

            prompt = domain_4_prompt(title=title, authors=authors)
            st.session_state.domain_4_response = get_chatgpt_response(prompt, pdf_text)

        # Always display Domain 4 Response if it exists
        if st.session_state.domain_4_response:
            st.write("**Domain 4 Response:**")
            st.write(st.session_state.domain_4_response)