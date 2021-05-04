# Source : https://leetcode.com/problems/project-employees-i/submissions/
SELECT p.project_id, round(avg(e.experience_years),2) as average_years from project p
inner join employee e on p.employee_id = e.employee_id
group by p.project_id
