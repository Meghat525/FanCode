from fancode_libs.api import TypiCodeController

class TestTodoCompletionHelper:
    def setup_method(self):
        self.typi_code_controller = TypiCodeController()
    def is_user_city_fancode(self, user_dict):
        lat = float(user_dict["address"]["geo"]["lat"])
        lng = float(user_dict["address"]["geo"]["lng"])
        if lat > -40 and lat < 5 and lng > 5 and lng < 100:
            return True
        return False

    def get_completion_percentage(self, all_todos, fancode_user_ids):
        todo_completion_percent = {}
        for todo_item in all_todos:
            if todo_item["userId"] in fancode_user_ids:
                is_completed = 0
                if todo_item["completed"] == True:
                    is_completed = 1
                if todo_item["userId"] not in todo_completion_percent:
                    todo_completion_percent[todo_item["userId"]] = 0
                todo_completion_percent[todo_item["userId"]] = (todo_completion_percent[todo_item["userId"]] + is_completed)/(todo_completion_percent[todo_item["userId"]] + 1)
        return todo_completion_percent

