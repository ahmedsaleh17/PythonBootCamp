
""""
For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. 
However, let's also include 10% wiggle room (deducted from the candidate's minimum salary) 
"""


def job_matching(candidate, job):
    """
    :param1 candidate: the developer who searching for matching job 
    :param2 job: the job specifications 
    :return Boolean Valure 
        True: if candidate minimum salary <= Job maximum salary 
    """

    return candidate['min_salary']*0.9 <= job['max_salary']




if __name__ == "__main__":
    
    candidate1 = {"min_salary": 120000}
    candidate2 = {"min_salary": 190000}
    job1 = {"max_salary": 130000}
    job2 = {"max_salary": 80000}
    job3 = {"max_salary": 171000}


    assert job_matching(candidate1, job1) == True
    assert job_matching(candidate1, job3) == True
    assert job_matching(candidate1, job2) == False
    assert job_matching(candidate2, job1) == False 

    
