from pathlib import Path
import streamlit as st
from PIL import Image

#----- PATH Setting-------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_file = current_dir / "style" / "main.css"
PDF_file = current_dir / "assets" / "CV.pdf"
PROFILE_file = current_dir / "assets" / "me.jpg"


#----- General Setting -----#
PAGE_TITLE = "Kong Sophareach"
PAGE_ICON = "💠"
NAME = "Kong Sophareach"
DESCRIPTION = """
Accomplished Business Analyst Project Manager with a verifiable track record of managing software implementation projects and exceeding expectations system documentation, developer interfacing, testing, and implementation project management with extensive financial experience.
"""

EMAIL = "sophareach.kong@outlook.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/sophareach-kong/",
    "Telegram": "https://www.t.me/sophareach3301",
    "Facebook": "https://www.facebook.com/sophareach"
}
EDUCATION = ""
CONTACT = {
    "Phone": "&nbsp; &nbsp; &nbsp;  📞 + (855) 98 547 775",
    "Email": "&nbsp; &nbsp; &nbsp; &nbsp; 📧 sophareach.kong@outlook.com",
    "Whatsapp": "📪 Sophareach | (+855) 98 547 775",
    "Address": "&nbsp; &nbsp; 🏡 St 112D, Phum Kva, Sangkat Dangkor, Khan Dangkor, Phnom Penh Cambodia"
}

#---- Page Configuration----
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered"
    )

#---- LOAD CSS and PDF---
with open(CSS_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(PDF_file, "rb") as pdf_file:
    PDFByte = pdf_file.read()

profile_pic = Image.open(PROFILE_file)


#----- Function -----
def btnHyerlink(clicked,link):
    st.success("yayy")

#----- Code -------
#----> HERO Section----
col1,col2 = st.columns([1,2])

with col1:
    st.image(profile_pic,width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFByte,
        file_name=pdf_file.name,
        mime="application/octet-stream",
        use_container_width=True
    )
    # st.write("✉️",EMAIL)

#----> SOCIAL Section----
st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate (SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    # cols[index].button(
    #     label=f"{platform}",
    #     on_click=btnHyerlink(False,f"{link}"),
    #     use_container_width=True,
    #     key=f"{index}"
    #     )

# for platform,link in SOCIAL_MEDIA.items():
#     st.button(
#         label=f"{platform}",
#         on_click=st.success("yayy")
#     )

#----> Education Section----
st.write("#")
st.subheader("Education")
st.write("---")
st.write("""
- 🎓 Highschool : American Intercon School | Graduated
- 🎓 Bachelor : SETEC Institute | Management Information System | Graduated
- 🎓 English Beginner to Advance : Aii Langugage Center | Level 12 | Graduated
- 🎓 English Supplement : ACE International School | Level 11B | Finished
- 🎓 Master : SETEC Institute | Master Information System | Studying

""")

#----> Hard Skill Section ----
st.write("#")
st.subheader("Hard Skills")
st.write("---")
st.write("""
- 🔎 Research (Security, technology, data analysis, etc)
- 🗣️ Technical Communication
- 🧑‍💼 Project Management
- 🧑‍💻 Document Development
- 👑 Leadership
- 🔦 Technical Problem solving
""")

#----> Professional Section ----
st.write("#")
st.subheader("Professional Experience")
st.write("---")
st.write("💠","**BUSINESS ANALYST | FinTech & Mobile Banking, Orbit Technology Solution**")
st.write("🗓️","10/2022 - Present")
st.write("""
- ✅ Assistant Project Manager & Business Analyst for large, complex FIN-Tech projects managing requirements to project delivery phase.
- ✅ Maintain perspective and a big picture project view amidst complex project details, and synthesize/translate key concerns, issues, risk, opportunities and impact back to the business.
- ✅ Lead the project team in the review of deliverables and project tracking of team activities. Oversaw all phases of various projects from initiation, planning and risk analysis, design, execution and project closure.
- ✅ Oversee all requirement analysis, use case identification, developing software requirement specification, workflows & wire frames of below projects.
- ✅ Performed the UX/UI design and development reviews of web and mobile applications.
- ✅ Interfaced with the client as part of requirements gathering and elicitation to finalize the project scope.
- ✅ Develop client application integration vision and oversee the business process and technical mapping.
- ✅ Assisted the project owner to develop both high-level and detailed application architecture to meet user requests and business needs.

""")

st.write("💠","**PROJECT SPECIALIST | Banking Financial Services & Insurance (BFSI), eCam Solution Co.,LTD**")
st.write("🗓️","Nov 2021 – Sep 2022")
st.write("""
- ✅ Monitoring and evaluating the overall Card Management System project implementation.
- ✅ Involved in more than 4 card management system (CMS) projects implementation for various MFIs and Banks
- ✅ Analysing project data and producing insights to optimize performance. Identifying problems and shortfalls and proposing solutions.
- ✅ Preparing, reviewing, and maintaining project documentation and reports.
- ✅ Developing tools for better project coordination and project management.
- ✅ Adjust Business Requirement Document, Functional Specification Document to identify flaws, missed requirement, scoping request, consult operational and technical to client of the project.
- ✅ Arranging conference calls to discuss issues within projects
- ✅ Working as a middleman to ensure communication flow and tracking the process of the project
- ✅ Managed and facilitated on developing testing (SIT) and user end testing (UAT)

""")

st.write("💠","**TECHNICAL ENGINEER | Business Banking Solution, eCam Solution Co.,LTD**")
st.write("🗓️","Oct 2020 – Oct 2021")
st.write("""
- ✅ Working with and under the supervision of the Solution director, initiated and iteratively developed effective solution that requires technical.
- ✅ Investigate issues, bugs, errors and collect logs within the system to send to vendor for resolution.
- ✅ Created and participated on User Acceptance Test Case (UAT) for ATM scenarios, Customer on-boarding, Card operation, system functional base and restrictions...etc.
- ✅ Review Business Requirement Document, Functional Specification. Document to identify flaws, possible bug, missed requirement, scoping of the project.
- ✅ On-site card management system installation for MFI and banks.

""")

#----> Volunteer Section ----
st.write("#")
st.subheader("Volunteer Experince")
st.write("---")

st.write("💠","**IT SUPPORT | IT & Maintenance Room, SETEC Institute**")
st.write("🗓️","Jul 2019 – Nov 2019")
st.write("""
- ✅ Accept student desktops, laptops, and other electronic devices for repair and maintenance. Request information about software and hardware issues and document all concerns.
- ✅ Troubleshooting systems and work with other colleague to determine hardware needed and software changes.
- ✅ Break down systems, remove malfunctioning hardware, install new parts. Perform all repairs and utmost concerns for user privacy.

""")

st.write("💠","**LC Vice President of Marketing & Communication | LC Phnom Penh, AIESEC Cambodia**")
st.write("🗓️","Aug 2018 – Feb 2020")
st.write("""
- ✅ Worked with more than 50+ people in communication flow, marketing campaign, creating attractive contents.
- ✅ Executed operation base on plans divided in semesters, terms (annual) Analysed current data and old relevant data (SWOT analysis) for a strategic planning.
- ✅ Managed a team of up to 6 people in each semester to execute plans and base on strict timeline.
- ✅ Participated, organized, facilitated, planned both local and international conferences with up to 20 people in a team.
- ✅ Negotiated with international entity to make relationship for a better performance and results.

""")

#----> Contact Section -----
st.write("#")
st.subheader("Find me")
st.write("---")

for platform,content in CONTACT.items():
    st.write(f"- {platform}: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **{content}**")
