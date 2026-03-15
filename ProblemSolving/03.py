def job_match(candidates, job):
    """
    Filters candidates based on equity requirements and location preferences.

    This function matches job candidates to job openings by evaluating:
    1. Equity requirements: If a candidate desires equity, the job must offer it
    2. Location match: Candidate's current or desired locations must match job locations

    Args:
        candidates (list): A list of candidate dictionaries containing:
            - desires_equity (bool): Whether the candidate wants equity compensation
            - current_location (str): Candidate's current work location
            - desired_locations (list): List of locations candidate is willing to work
        job (dict): A job opening dictionary containing:
            - equity_max (float): Maximum equity offered (0 means no equity)
            - locations (list): List of job locations available

    Returns:
        list: A list of candidate dictionaries who match both equity and location criteria
    """
    profiles_matches = []

    for cand in candidates:
        # Skip candidates if they want equity but the job doesn't offer any
        if cand["desires_equity"]:
            if job["equity_max"] == 0:
                continue

        # Check if candidate's location matches job locations
        # Match occurs if current location is in job locations OR
        # any of candidate's desired locations overlap with job locations
        if (
            cand["current_location"] in job["locations"]
            or len(set(cand["desired_locations"]).intersection(job["locations"])) != 0
        ):
            # Add matching candidate to results
            profiles_matches.append(cand)

    return profiles_matches


if __name__ == "__main__":

  # test cases

  candidates = [
      {
          "desires_equity": True,
          "current_location": "New York",
          "desired_locations": ["San Francisco", "Los Angeles"],
      },
      {
          "desires_equity": False,
          "current_location": "San Francisco",
          "desired_locations": ["Kentucky", "New Mexico"],
      },
  ]

  job1 = {"equity_max": 0, "locations": ["Los Angeles", "New York"]}
  job2 = {"equity_max": 1.2, "locations": ["New York", "Kentucky"]}

  assert len(job_match(candidates, job1)) == 0
  assert len(job_match(candidates, job2)) == 2
