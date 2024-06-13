# SQLite

## Wywołanie komend SQLite za pomocą skryptu w pythonie  

W poniższym kodzie funkcja `create_connectrion()` tworzy połączenie z plikiem z bazy danych oraz wyświetla wyniki. `sql_query()` zwraca kod *SQL*. 

```py
import sqlite3
from sqlite3 import Error

def create_connectrion(filename):
    conn = sqlite3.connect(filename)
    try:
        c = conn.cursor()
        c.execute(sql_query())
        for row in c.fetchall():
            print(row)
    except Error as e:
        print(e)
    conn.close()

def sql_query():
    return """select * from little_penguins;"""


if __name__ == '__main__':
    create_connectrion("sql-tutorial/db/penguins.db")
```
W rezultacie wywołania kodu, otrzymujemy następujące wyniki:  
![alt text](imgs/image.png)  


Na potrzeby wykonania zadań, dla zwiększenia czytelności wyników, skrypty *sql* zostaną wykonane za pomocą programu `DB Browser for SQLite`. Poniżej ten sam wynik w tym programie:  
![alt text](imgs/image-1.png)  

## Zadania z tutoriala  

1. Specyfikowanie kolummn:  
![alt text](imgs/image-2.png)

2. Sortowanie  
![alt text](imgs/image-3.png)  

3. Limitowanie liczby wyników  
![alt text](imgs/image-4.png)  

4. Przesunięcie wyników  
![alt text](imgs/image-5.png)  

5. Usuwanie duplikatów  
![alt text](imgs/image-6.png)  

6. Filtrowanie wyników  
![alt text](imgs/image-7.png)  

7. Złożone filtrowanie  
![alt text](imgs/image-8.png)  

8. Kalkulacje  
![alt text](imgs/image-9.png)  

9. Nazywanie kolumn  
![alt text](imgs/image-10.png)  

10. Kalkulacje z brakujacymi wartościami  
![alt text](imgs/image-11.png)  

11. Logika trójskładnikowa  
![alt text](imgs/image-12.png) ![alt text](imgs/image-13.png)  

12. Przechwytywanie wartośći *NULL*  
![alt text](imgs/image-14.png)

13. Agregacja - łączenie  
![alt text](imgs/image-15.png)  
![alt text](imgs/image-16.png)  
![alt text](imgs/image-17.png)  

14. Grupowanie  
![alt text](imgs/image-18.png)  

15. Niezaagregowane kolumny  
![alt text](imgs/image-19.png)  

16. Filtrowanie zaagregowanych wartości  
![alt text](imgs/image-20.png)  

17. Zwiększanie czytelności - Zaokrąglanie  
![alt text](imgs/image-21.png)  

18. Filtrowanie zaagragowanych wartości  
`filter()`  
![alt text](imgs/image-22.png)  

19. Tworzenie tabel  
```sql
create table job (
    name text not null,
    billable real not null
);
create table work (
    person text not null,
    job text not null
);
```  
![alt text](imgs/image-23.png)  

20. Wstawianie danych do tabeli  
```sql
insert into job values
('calibrate', 1.5),
('clean', 0.5);
insert into work values
('mik', 'calibrate'),
('mik', 'clean'),
('mik', 'complain'),
('po', 'clean'),
('po', 'complain'),
('tay', 'complain');
```  
![alt text](imgs/image-24.png)  

21. Aktualizacja rekordów  
```sql
update work
set person = 'tae'
where person = 'tay';
```  
![alt text](imgs/image-25.png)  

22. Usuwanie wierszy  
![alt text](imgs/image-26.png)  

23. Tworzenie kopii zapasowych  
![alt text](imgs/image-27.png)  

24. Złączenia  
>CROSS JOIN  
![alt text](imgs/image-28.png) ![alt text](imgs/image-29.png)  

>INNER JOIN  
![alt text](imgs/image-30.png) ![alt text](imgs/image-31.png)  

>Agregacja złączeń  
![alt text](imgs/image-32.png)  

>LEFT JOIN  
![alt text](imgs/image-33.png) ![alt text](imgs/image-34.png)  

>Agregacja Left Join  
![alt text](imgs/image-35.png)

>Coalescing Values  
Zwraca pierwszą wartość inną od *null*  
![alt text](imgs/image-36.png)  

25. Negacja  
![alt text](imgs/image-37.png)  

26. Przynależność elementu  
![alt text](imgs/image-38.png)  

27. Pozdzapytania  
![alt text](imgs/image-39.png)  

28. Klucz podstawowy  
![alt text](imgs/image-40.png)  

29. Autoinkrementacja klucza głównego  
![alt text](imgs/image-41.png)  

30. Altering Tables - dodawanie kolumn   
![alt text](imgs/image-42.png)  

31. Usuwanie tabel  
```sql
drop table work;
alter table new_work rename to work;
```  

32. Warukowe tworzenie tabeli  
![alt text](imgs/image-43.png)  

33. Filtrowanie wartości indywidualnych z agregowanymi  
![alt text](imgs/image-44.png)  

34. Comparing Individual Values to Aggregates Within Groups  
![alt text](imgs/image-45.png)  

35. Common Table Expressions  
![alt text](imgs/image-46.png)  

36. Explaining Query Plans  
![alt text](imgs/image-47.png)  

37. Enumerating Rows - Indeksy wierszy  
![alt text](imgs/image-48.png)  

38. Conditionals  
`iif(condition, true_result, false_result)`  
![alt text](imgs/image-49.png)  

39. Selecting a Case  
![alt text](imgs/image-50.png)  

40. Checking a Range  
![alt text](imgs/image-51.png)  

41. Pattern Matching  
![alt text](imgs/image-52.png)  

42. Selecting First and Last Rows  
![alt text](imgs/image-53.png)  

43. Intersection - podobne do where  
![alt text](imgs/image-54.png)  

44. Exclusion - wykluczenie  
![alt text](imgs/image-55.png)  

45. Random Numbers and Why Not  
![alt text](imgs/image-56.png)  

46. Self Join  
zwraca w tym przypadku wszystkie kombinacje  
![alt text](imgs/image-57.png)  

47. Existence and Correlated Subqueries  
![alt text](imgs/image-59.png)  

48. Nonexistence  
![alt text](imgs/image-60.png)  

49. Avoiding Correlated Subqueries  
![alt text](imgs/image-61.png)  

50. Lead and Lag  
![alt text](imgs/image-58.png)  

51. Windowing Functions  
![alt text](imgs/image-62.png)  

52. Partitioned Windows  
![alt text](imgs/image-63.png)  

53. Storing JSON  
![alt text](imgs/image-64.png)

54. Select Fields from JSON  
```sql
select
    details->'$.acquired' as single_arrow,
    details->>'$.acquired' as double_arrow
from machine;
```  
![alt text](imgs/image-66.png)  
![alt text](imgs/image-65.png)  

55. JSON Array Access  
```sql
select
    ident,
    json_array_length(log->'$') as length,
    log->'$[0]' as first
from usage;
```  
![alt text](imgs/image-67.png)  
![alt text](imgs/image-68.png)  

56. Unpacking JSON Arrays  
```sql
select
    ident,
    json_each.key as key,
    json_each.value as value
from usage, json_each(usage.log)
limit 10;
```  
![alt text](imgs/image-69.png)  
![alt text](imgs/image-70.png)  

57. Selecting the Last Element of an Array  
```sql
select
    ident,
    log->'$[#-1].machine' as final
from usage
limit 5;
```  
![alt text](imgs/image-71.png)  

58. Modifying JSON  
![alt text](imgs/image-72.png)  

59. Tombstones  
![alt text](imgs/image-73.png)  

60. Hours Reminder  
![alt text](imgs/image-74.png)  

61. Representing Graphs  
![alt text](imgs/image-75.png)  

62. Recursive Queries  
![alt text](imgs/image-76.png)  

63. Bidirectional Contacts  
```sql
create temporary table bi_contact (
    left text,
    right text
);

insert into bi_contact
select
    left, right from contact
    union all
    select right, left from contact
;
```  

64. Updating Group Identifiers  
![alt text](imgs/image-77.png)  

65. Recursive Labeling  
![alt text](imgs/image-78.png)  

### Python  

---

66. Querying from Python  
![alt text](imgs/image-81.png)  
![alt text](imgs/image-82.png)  

67. Incremental Fetch  
![alt text](imgs/image-83.png)  
![alt text](imgs/image-84.png)  

68. Insert, Delete, and All That  
![alt text](imgs/image-79.png)  
![alt text](imgs/image-80.png)  

69. Interpolating Values  
![alt text](imgs/image-85.png)  
![alt text](imgs/image-86.png)  

70. Script Execution  
![alt text](imgs/image-87.png)  
![alt text](imgs/image-88.png)  

71. SQLite Exceptions in Python  
![alt text](imgs/image-90.png)  
![alt text](imgs/image-89.png)  

72. Python in SQLite  
![alt text](imgs/image-91.png)  
![alt text](imgs/image-92.png)  

73. Handling Dates and Times  
![alt text](imgs/image-94.png)  
![alt text](imgs/image-93.png)  

74. Pandas and SQL  
instalacja biblioteki pandas:  
```bash
pip install pandas
```  
![alt text](imgs/image-95.png)  
![alt text](imgs/image-96.png)  

