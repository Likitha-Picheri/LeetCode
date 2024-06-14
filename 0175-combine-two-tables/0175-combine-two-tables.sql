# Write your MySQL query statement below
select lastname,firstname,city,state from person left join address on  person.personId=address.personId;
