from todo_completion_helper import TestTodoCompletionHelper


class TestTodoCompletion(TestTodoCompletionHelper):
    def test_task_complete_more_than_50_per(self, logger):
        all_todos = self.typi_code_controller.get_all_todos()
        all_users = self.typi_code_controller.get_all_users()
        print(all_todos[0])
        print(all_users[0])
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
            assert False, logger.info(f"{len(todo_completion_percent)} have less than 50% todos completed. Their ids with completion percentage are: {incomplete_todo_users}.")
