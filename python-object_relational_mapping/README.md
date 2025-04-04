# Python - Object-Relational Mapping

This project covers the basics of using Python to interact with relational databases using both raw SQL queries (MySQLdb) and ORM (SQLAlchemy).

## Files

### MySQLdb scripts:
- `0-select_states.py`: Lists all states from the database
- `1-filter_states.py`: Filters states starting with 'N'
- `2-my_filter_states.py`: Filters states by name (unsafe)
- `3-my_safe_filter_states.py`: Filters states by name (safe from SQL injection)
- `4-cities_by_state.py`: Lists all cities with their states
- `5-filter_cities.py`: Lists cities of a specific state

### SQLAlchemy scripts:
- `model_state.py`: State class definition
- `7-model_state_fetch_all.py`: Lists all State objects
- `8-model_state_fetch_first.py`: Prints the first State object
- `9-model_state_filter_a.py`: Lists State objects containing 'a'
- `10-model_state_my_get.py`: Gets a State by name
- `11-model_state_insert.py`: Adds a new State
- `12-model_state_update_id_2.py`: Updates a State's name
- `13-model_state_delete_a.py`: Deletes States with 'a' in name
- `model_city.py`: City class definition
- `14-model_city_fetch_by_state.py`: Lists all City objects with their State
