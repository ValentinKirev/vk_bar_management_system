from controllers.order_controller import OrderController


class CreateOrderCommand:
    def __init__(self, controller: OrderController, table_number):
        self.controller = controller
        self.table_number = table_number

    def __call__(self, *args, **kwargs):
        self.controller.create_order(self.table_number)
        print(f'Table number {self.table_number} order successfully created')