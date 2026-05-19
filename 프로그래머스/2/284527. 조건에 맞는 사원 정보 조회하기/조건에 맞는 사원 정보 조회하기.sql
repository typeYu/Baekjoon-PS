select sum(c.SCORE) as SCORE, c.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL
from HR_DEPARTMENT as a
join HR_EMPLOYEES as b on a.DEPT_ID = b.DEPT_ID
join HR_GRADE as c on b.EMP_NO = c.EMP_NO
group by c.EMP_NO
order by sum(c.SCORE) DESC
limit 1;