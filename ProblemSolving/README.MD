# Problem1: WeIrD StRiNg CaSe

Description:

Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
Examples:
```
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
```

[WeIrD StRiNg CaSe solution](01.py) 


-------------------------------------------------

# Problem2: Job Matching #1

Description:

Let's build a matchmaking system that helps discover jobs for developers based on a number of factors.

One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we generally have a rough idea of the minimum salary we would be satisfied with.

Let's give this a try. We'll create a function match (job_matching in Python) which takes a candidate and a job, which will return a Boolean indicating whether the job is a valid match for the candidate.

A candidate will have a minimum salary, so it will look like this:
```
candidate = {
  'min_salary': 120000
}
```

A job will have a maximum salary, so it will look like this:
```
job = {
  'max_salary': 140000
}
```
If either the candidate's minimum salary or the job's maximum salary is not present, throw an error.

For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. However, let's also include 10% wiggle room (deducted from the candidate's minimum salary) in case the candidate is a rockstar who enjoys programming on Codewars in their spare time. The company offering the job may be able to work something out. 

[Job Matching #1 Solution](02.py)

--- 
# Problem3: Job Matching #2 
Description:

Consider a matchmaking system that is designed to deliver jobs to software developers on a continual basis. As more quality jobs are handpicked into the system, they will be matched to all the enrolled developers; affording them better opportunities daily.

This means that somewhere in the system there exists functionality to take a job and match it against enrolled candidates. There are several factors that go into this matching, but we'll focus on two for the purposes of this Kata.

Create a function match which takes a job, and filters a list of candidates to the ones that match the job. We'll focus on two matching properties for this Kata: equity and location.
Equity

The candidate has an equity property (boolean) indicating if they desire equity, while the job will have a maximum equity property (float) representing the max amount of equity offered. If the maximum equity is zero, we can infer there is no equity offered. A job will match unless the candidate desires equity, but the job does not offer any.
Location

The candidate will have two location properties: current location and desired locations. A job can be located in multiple places as well which will be represented by its locations property. A match is when a job location is either in the candidate's current location or any of the candidate's desired locations.

So the candidate list might look like this:

```
candidates = [{
  'desires_equity': True,
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, ...]
```

And a job might look like this:

```
job = {
  'equity_max': 1.2,
  'locations': ['New York', 'Kentucky']
}
```

[Job Matching #2 Solution](03.py)