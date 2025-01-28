import openai
import streamlit as st
import pandas as pd
import requests
import pymupdf4llm
import pymupdf
import re
from requests.utils import quote
import json

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = pymupdf.open(stream=pdf_file.read(), filetype="pdf")
    text = pymupdf4llm.to_markdown(doc)
    return text

def get_chatgpt_response(prompt, pdf_text):
    from openai import OpenAI
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"""You are a helpful assistant. 
         
We have developed a list of questions that can establish whether a randomised control trial 
is trustworthy. I will first give you some information about this protocol:

Motivation for INSPECT-SR
Systematic reviews exploring health interventions aim to include all relevant randomised controlled trials (RCTs), appraising and synthesising this evidence to arrive at an overall conclusion about whether an intervention works and whether it causes harm. Problematic studies pose a threat to the evidence synthesis paradigm. These are defined by Cochrane as “any published or unpublished study where there are serious questions about the trustworthiness of the data or findings, regardless of whether the study has been formally retracted”(1, 2). Studies may be problematic because they include some false data or results, or may be entirely fabricated. Research misconduct is just one possible explanation for false data. Another possibility would be the presence of catastrophic failures in the conduct of the study, such as miscoding of patient conditions (e.g., inverting active treatment and placebo conditions), failure in the computerised randomisation service, or severe errors in the analysis code. Whether they are the result of deliberate malpractice or honest error, these issues may not be immediately apparent to journal editors and peer reviewers. Consequently, problematic studies may be published, and subsequently included in systematic reviews. Studies are routinely appraised on the basis of their methodological validity during the systematic review process. However, these assessments are predicated on the assumption that the studies and the data they are based on are authentic, and also that the authors did not make any major errors during data collection, analysis or reporting. In fact, many reports of problematic studies describe sound methodology, and so are not flagged by critical appraisal tools.
This prompts the question of how we can identify problematic studies. The INSPECT-SR (INveStigating ProblEmatic Clinical Trials in Systematic Reviews) tool has been developed for this purpose, using empirical evidence and consensus methodology. The development process has been described in a protocol paper [REF]. The tool can be used to assess the trustworthiness of RCTs. 

Overview of the draft INSPECT-SR tool
The INSPECT-SR tool guides the user through a series of 21 checks in four domains to help them make a judgement about the trustworthiness of a study. In this context, trustworthiness does not encompass internal or external validity, as assessed using Risk of Bias tools and GRADE, nor does it include conflicts of interest. The four domains in the tool are:
 1) Inspecting post-publication notices
 2) Inspecting conduct, governance and transparency
 3) Inspecting text and figures
 4) Inspecting results in the study
 The checks in each domain assist the reviewer in identifying any domain-level concerns relating to trustworthiness. The user may then use the domain-level judgement to arrive at an overall judgement about the trustworthiness of a study. We emphasise that concerns about a study’s trustworthiness do not amount to an accusation of misconduct. INSPECT-SR is not concerned with determining whether inauthentic data have arisen due to deliberate misconduct or honest error.

Application of the draft INSPECT-SR tool to assess an individual study
Users are advised to use the checks in each domain to arrive at a domain-level judgement of trustworthiness. For each domain, the user records a judgement of “no concerns”, “some concerns”, or “serious concerns”. The purpose of the tool is to identify potentially problematic studies, and a user may decide they have sufficient concerns about a study without having completed all of the checks included in the draft tool.  The user should terminate the assessment of a study if they consider a judgement of ‘serious concerns’ to be warranted at any point during the assessment. This conclusion could be reached before all domains have been assessed. Furthermore, the user might decide that they have serious concerns in relation to a particular domain having completed only a subset of the checks in that domain. In this situation, it would not be necessary to complete the remaining checks in the domain. This differs from Risk of Bias tools, where the expectation is that all domains should be assessed for each study.
Having made a judgement in relation to all four domains (or having reached a judgement of “serious concerns” in relation to any of the first three, if the user has opted to terminate the assessment on this basis) the user is required to make an overall judgement about the trustworthiness of the study, again using the options “no concerns”, “some concerns”, or “serious concerns”. It is expected that the overall judgement for a study will be at least as severe as the judgement for the domain with the most severe rating. For example, where one domain has been rated as “serious concerns”, it is expected that the overall study judgement will also be one of “serious concerns”. If the most severe domain-level judgement is “some concerns”, then it is expected that the overall study-level judgement should be at least “some concerns”, but the cumulative impact of judging there to be “some concerns” in several domains may be sufficient to warrant an overall judgement of “serious concerns” for the study. Users are encouraged to record the reasons for their domain and study-level judgements, to permit scrutiny. We envision that INSPECT-SR assessments will be published as part of the systematic review, to ensure transparency.
Figure 1 illustrates the structure of the draft INSPECT-SR tool. A study may be reported across several publications, including conference abstracts, preprints, protocol papers, and secondary analysis papers. As for Risk of Bias assessment, it may be necessary to consider several of these to obtain the information necessary to complete the checks. The final check in the draft tool explicitly asks the user to consider whether there are any contradictions in information reported in different publications relating to the index study.

Incorporating the draft INSPECT-SR tool into the systematic review process
The draft INSPECT-SR tool has been designed to be implemented in the context of the Cochrane policy for managing potentially problematic studies (https://www.cochranelibrary.com/cdsr/editorial-policies/problematic-studies-implementation-guidance ). 
The draft INSPECT-SR tool should be applied prior to Risk of Bias assessment of eligible studies, regardless of which tool is used for this purpose. Where a study is judged to warrant “serious concerns”, it should be excluded from the review. Studies which receive a study-level judgement of “some concerns” should not be automatically excluded, but it is recommended that these studies should be subjected to sensitivity analysis to determine their influence on the results and conclusions of the review. As for Risk of Bias assessment, there are several possibilities for how this could be operationalised, and systematic review teams should specify their approach at the protocol stage. Possibilities include: 1) restricting the primary analysis to studies with a study-level judgement of “no concerns”, and including studies with a study-level judgement of “some concerns” in a sensitivity analysis, and 2) including studies with a study-level judgement of “some concerns” in the primary analysis and performing a sensitivity analysis restricted to studies with a study-level judgement of “no concerns”.  A third possibility is to stratify a meta-analysis according to study-level judgement.
As with other aspects of data extraction and critical appraisal of studies during the conduct of a systematic review, correspondence with study authors may be useful to clarify points of uncertainty in relation to trustworthiness assessment, and should be attempted by review authors.  Cochrane guidance includes specific instructions for contacting authors and editors (https://www.cochranelibrary.com/cdsr/editorial-policies/problematic-studies-implementation-guidance ).

Brief guidance on the use of individual checks in the draft INSPECT-SR tool
The following describes key points to consider in relation to individual checks in the draft INSPECT-SR tool. Full guidance will be developed to accompany the final version of the tool. There are four response options corresponding to each check: “Yes”, “No”, “Unclear”, “NA” (Not Applicable). Checks have been worded such that a positive response (“Yes”) corresponds to a potentially problematic feature. Generally, domain-level judgements do not follow from check responses in a deterministic or algorithmic fashion. For example, we have not specified a threshold corresponding to the number of checks that should be failed (response of “Yes”) to trigger domain-level judgements of “serious concerns”. Nonetheless, there are several checks for which a positive response will generally suffice to warrant a judgement of “serious concerns” for the domain and for the study as a whole. These are described in the brief guidance below. The purpose of the checks is to help the user reach a domain-level judgement about whether or not they have concerns about trustworthiness, and to articulate a basis for that judgement. It is recommended to record some explanatory text detailing the reason for the check response. Some of the checks may be difficult to assess without topic expertise, and a comprehensive assessment is likely to require input from a well-rounded review team. We use the term “index study” to refer to the study being assessed using the draft INSPECT-SR tool.

You are here to help me with the following article:
{pdf_text}
"""},
        {"role": "user", "content": prompt}
    ]
    )
    return completion.choices[0].message.content

# Function to get first author and title using OpenAI API
def get_authors_and_title(pdf_text):
    prompt = (
        "Extract the authors and title from the provided text. "
        "Answer strictly in the following format, including the single quotes:\n"
        "Authors: 'author 1; author 2; author 3; etc.'\n"
        "Title: 'name of the title'"
    )
    response = get_chatgpt_response(prompt, pdf_text)
    print(response)
    
    # Use regular expressions to extract authors and title
    authors_match = re.search(r"Authors:\s*'(.*?)'", response, re.DOTALL)
    title_match = re.search(r"Title:\s*'(.*?)'", response, re.DOTALL)
    
    # Extract or set default values if not found
    authors = authors_match.group(1).strip() if authors_match else "Authors not found"
    title = title_match.group(1).strip() if title_match else "Title not found"
    
    return authors, title

def check_retraction_status(paper_title):
    # Convert the paper title to lowercase for case-insensitive comparison
    paper_title_lower = paper_title.lower()
    retracted_paper = st.session_state.retraction_watch_df[st.session_state.retraction_watch_df['Title'].str.lower().str.contains(paper_title_lower, na=False)]
    if not retracted_paper.empty:
        return "Yes", retracted_paper.iloc[0].to_dict()
    return "No", None

def check_expression_of_concern(paper_title):
    # Convert the paper title to lowercase for case-insensitive comparison
    paper_title_lower = paper_title.lower()
    retracted_paper = st.session_state.retraction_watch_df[st.session_state.retraction_watch_df['Title'].str.lower().str.contains(paper_title_lower, na=False)]
    if not retracted_paper.empty:
        if 'expression of concern' in retracted_paper.iloc[0]['RetractionNature'].lower():
            return "Yes"
    return "No"

def check_author_track_record(author_name):
    # Convert the author name to lowercase for case-insensitive comparison
    author_names = [name.strip().lower() for name in author_name.split(';')]
    retracted_papers = st.session_state.retraction_watch_df[
        st.session_state.retraction_watch_df['Author'].str.lower().apply(
            lambda authors: any(author in authors for author in author_names)
        )
    ]
    if not retracted_papers.empty:
        return "Yes", retracted_papers.to_dict('records')
    return "No", None

def search_clinical_trials_full(title):
    # Limit the title to the first 5 words for search query
    title_query = " ".join(title.split()[:7])
    encoded_query = quote(title_query)
    
    # Construct the API URL
    url = f"https://clinicaltrials.gov/api/v2/studies?query.titles={encoded_query}&format=json"
    print(f"Query URL: {url}")  # Log for debugging
    
    try:
        # Send the request to the API
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            studies = data.get("studies", [])
            
            if studies:
                # Return the full JSON data of the first study
                return studies[0]  # First matching study
            else:
                return {"Error": f"No studies found matching the given title '{title.split()[:7]}' (first 7 words)."}
        
        elif response.status_code == 400:
            return {"Error": f"Bad request. Query might be malformed: {url}"}
        
        elif response.status_code == 404:
            return {"Error": "API endpoint not found. Check the URL or API version."}
        
        else:
            return {"Error": f"API error. Status code: {response.status_code}"}
    
    except requests.exceptions.RequestException as e:
        return {"Error": f"Network error: {str(e)}"}