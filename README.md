## FANCODE AUTOMATION SUITE ##

### Intro ###
The assigned task to automate the following test case:
"All the users of City `FanCode` should have more than half of their todos task completed."
is completed in python.
The pytest module is used to achieve this.

### Directory Structure ###
- **FanCode/**
  - **fancode_libs/** --This folder is supposed to have the all common code that will be used by the rest of the test cases.
    - `__init__.py`
    - **api/** --This folder is supposed to have all the apis.
      - `__init__.py`
      - `typicontroller.py` --This file has the 2 apis from the resources provided as currently only 2 are used.
  - **fancode_tests/** --This folder is supposed to have all test folders.
    - **test_todo_completion/** --This folder is specific to todo completion test cases.
      - `__init__.py`
      - `test_todo_completion.py` --This has the main test case.
      - `todo_completion_helper.py` --Helper functions are added in this file to make test file less bulky.
  - `conftest.py` --This file runs at the beginning and sets up the logger and also the path so as imports work properly.

### How to Run the Test ###
1. Setup Python on you machine.
2. Change your directory to FanCode and install the requirement:`pip install -r requirements.txt`.
3. Run the following command: `fancode_tests\test_todo_completion\test_todo_completion.py`.
4. This case will only pass if all the users of fancode city have more than 50% of their todos completed. Otherwise, it will fail giving the user ids of the users having completion percentage not more than 50%. Their completion percentage will also be displayed. 

The current output looks like:
``` 
py.test -sv fancode_tests\test_todo_completion\test_todo_completion.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\User\PycharmProjects\FanCode\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\User\PycharmProjects\FanCode
collected 1 item                                                                                                                                   

fancode_tests/test_todo_completion/test_todo_completion.py::TestTodoCompletion::test_task_complete_more_than_50_per 2024-10-10 23:10:03,993 - INFO - User ids of User that belongs to the city FanCode: [1, 5, 10]
2024-10-10 23:10:03,993 - INFO - 2 user(s) don't have more than 50% todos completed. Their ids with completion percentage are: {5: 33.33333333333333, 10: 50.0}.
FAILED

==================================================================== FAILURES ===================================================================== 
_____________________________________________ TestTodoCompletion.test_task_complete_more_than_50_per ______________________________________________ 

self = <test_todo_completion.TestTodoCompletion object at 0x00000253DE70FDA0>, logger = <Logger conftest (INFO)>

    def test_task_complete_more_than_50_per(self, logger):
        all_todos = self.typi_code_controller.get_all_todos()
        all_users = self.typi_code_controller.get_all_users()
        fancode_user_ids = []
        for user_dict in all_users:
            if self.is_user_city_fancode(user_dict):
                fancode_user_ids.append(user_dict["id"])
        logger.info(f"User ids of User that belongs to the city FanCode: {fancode_user_ids[:5]}")
        todo_completion_percent = self.get_completion_percentage(all_todos, fancode_user_ids)
        incomplete_todo_users = {}
        for user_id in todo_completion_percent:
            if todo_completion_percent[user_id] <= 0.5:
                incomplete_todo_users[user_id] = todo_completion_percent[user_id]*100
        if len(todo_completion_percent) > 0:
>           assert False, logger.info(f"{len(incomplete_todo_users)} user(s) don't have more than 50% todos completed. Their ids with completion percentage are: {incomplete_todo_users}.")
E           AssertionError: None
E           assert False

fancode_tests\test_todo_completion\test_todo_completion.py:19: AssertionError
---------------------------------------------------------------- Captured log call ---------------------------------------------------------------- 
INFO     conftest:test_todo_completion.py:12 User ids of User that belongs to the city FanCode: [1, 5, 10]
INFO     conftest:test_todo_completion.py:19 2 user(s) don't have more than 50% todos completed. Their ids with completion percentage are: {5: 33.33333333333333, 10: 50.0}.
============================================================= short test summary info ============================================================= 
FAILED fancode_tests/test_todo_completion/test_todo_completion.py::TestTodoCompletion::test_task_complete_more_than_50_per - AssertionError: None   
================================================================ 1 failed in 1.87s ================================================================  
```