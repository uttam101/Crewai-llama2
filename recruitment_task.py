from crewai import Task 
from textwrap import dedent
class RecruitmentTask():
    
    def jd_creation(job_roll , experience , skills ,agent):
        return Task(
            name="JD Creation",
            description=dedent(f"""
                Create best job description based on this particular job position.
                These are the basic details of this role
                skills: {skills}
                experience: {experience} years
                job_roll: {job_roll}
            """),
            # expected_output=dedent(f"""create a best job description for this particular role and please make sure the keep the output in json or format in any format so that i can take the output and convert it into json or any other format.
            #     summery(small description about the job role)
            #     roles and responsibilities in this job role
            #     requirements (required skill and experience for this role)

            # """),
            expected_output=dedent(f"""create a best job description for this particular role and apart from this {skills} skills
            make sure to take inspriration from market research if needed and please make sure the keep the output in structured format so that i can later take the output and convert it into json.
                summery(small description about the job role)
                roles and responsibilities in this job role
                requirements (required skill and experience for this role)
            """),
            agent = agent,
            # output_file = "job_description.json",
            # output="json"
        )

    def market_research(job_roll, experience, agent):
        return Task(
            name="Market Research",
            description=dedent(f"""
                Research about what is the current industry demand, market opportunities and trends for {job_roll} role with {experience}.
            """),
            expected_output=dedent(f"""
                create a summery report of your research about the current market demand and requirement for this particular role.
            """),
            agent = agent
        )


