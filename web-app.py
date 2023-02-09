import requests
from pathlib import Path
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "style.css"
resume_file = current_dir / "images" / "CV.pdf"

st.set_page_config(page_title="Pranshu Ghildiyal | DevOps", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl(
    "https://assets3.lottiefiles.com/private_files/lf30_4y2cuiyr.json")
lottie_aws = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_hweqrado.json")
lottie_jenkins = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_liq7vebf.json")
lottie_aws2 = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_kxaxahzd.json")
lottie_hello = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_uqeyp3tb.json")
lottie_load = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_p8bfn5to.json")


# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns((1, 3))
    with left_column:
        st_lottie(lottie_hello, height=150, key="hello")
    with right_column:
        st.subheader("Hi, I'm Pranshu :wave: :smile:")
        st.title("A Cloud/DevOps Enthusiast From :blue[India] 🇮🇳")

# ---- ABOUT ME ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.header("About Me :smile:")
        st.write(
            """
            A highly motivated and detail-oriented professional with a strong background in computer science and a passion for Cloud Technologies & DevOps.\n
            Proficient in AWS Suite with experience in Virtualization, Automation, Continuous Integration and Delivery, Infrastructure as Code and relevant tools such as Jenkins, Docker, Kubernetes, Terraform etc. \n
            Strong problem-solving skills and a willingness to continuously learn and adapt to new technologies. \n
            Seeking to start a career in DevOps and contribute to the growth and success of a dynamic DevOps team.\n
            If this sounds interesting to you, consider connecting with me or sending me a message.(Links Below).
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_aws, height=300, key="coding_aws")
    with text_column:
        st.subheader("AWS Lift And Shift")
        st.write(
            """
            ○ Successfully migrated a Java web application to the AWS cloud using a variety of AWS services, including EC2, ELB,
Auto-Scaling Group, Route 53, CloudFront, Elastic Beanstalk, CloudWatch, RDS, ElastiCache, and AmazonMQ,
showcasing strong knowledge of cloud infrastructure and best practices. \n
○ Re-architected the application using Elastic Beanstalk and CloudFormation, demonstrating knowledge of PaaS, SaaS and
IaC along with Implementing security best practices by using Security Groups and Key-Pairs, showing understanding of
cloud security.\n
○ Improved performance and scalability by using ElastiCache and AmazonMQ, demonstrated knowledge of messaging
queues and caching and showcased ability to work with multiple technology stacks including AWS, Java, Nginx, Apache Tomcat, RabbitMQ, Memcached, MySQL, and Linux.
            """
        )
        st.markdown("[Check It Out...](https://github.com/PranshuGhildiyal)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_aws2, height=300, key="coding_aws2")
    with text_column:
        st.subheader("CI/CD With AWS Suite")
        st.write(
            """
            ○ Demonstrated experience with building a complete CI/CD pipeline using AWS services such as Code Commit, Code
Build, Code Deploy, Beanstalk, RDS, and pipeline, showcasing knowledge of AWS services and their integration to build
a pipeline.\n
○ Utilized AWS Code Build and Code Deploy to automate the build and deployment process, showcasing experience with
continuous integration and delivery.\n
○ Improved the performance and scalability of the application by integrating Beanstalk, RDS, and pipeline, showcasing
knowledge of PaaS, IaaS and best practices, also implemented version control and build processes using Code Commit and Code Build, and streamlined the deployment process by automating it with Code Deploy and Beanstalk, showcasing knowledge of deployment automation and best practices.

            """
        )
        st.markdown("[Check It Out...](https://github.com/PranshuGhildiyal)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_jenkins, height=300, key="coding_jenkins")
    with text_column:
        st.subheader("CI/CD With Jenkins")
        st.write(
            """
            ○ Successfully implemented a continuous integration and delivery pipeline using Jenkins, SonarQube, Docker, Nexus, ECS,
Fargate, and ECR, showcasing strong knowledge of pipeline management and best practices.\n
○ Used Jenkins to automate the build, test and deployment of software, while also maintaining Jenkins master-slave architecture to improve build efficiency and scalability, demonstrating experience with load balancing and distributed systems and incorporated SonarQube to ensure code quality and security, demonstrating understanding of code analysis,
and how to detect and prevent software bugs and vulnerabilities.\n
○ Utilized Docker, Nexus, and ECR to containerize the application and improve its portability and scalability, showcasing
knowledge of containerization and microservices.
            """
        )
        st.markdown("[Check It Out...](https://github.com/PranshuGhildiyal)")

st.write("##")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_load, height=50, key="load")
    with text_column:
        st.subheader("Coming Soon...")

# ---- CONTACT ----
with st.container():
    st.write("---")
    left_column, space, right_column = st.columns((1.5, 0.33, 1))
    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/pranshuxwork+portfolio@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Full Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    with left_column:
        st.header("Let's have a chat!")
        st.write("Connect with me on the following links 👉🏻")
        st.write("Or send me a message directly 👇🏻")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:

        st.subheader(":link: Links : ")
        st.write("➡️[Email](mailto:pranshuxwork+portfolio@gmail.com)\n")
        st.write("➡️[GitHub](https://www.github.com/PranshuGhildiyal)\n")
        st.write("➡️[LinkedIn](https://www.linkedin.com/in/pranshughildiyal)\n")
        st.subheader("✉️ Downloads : ")
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(
                label="📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
