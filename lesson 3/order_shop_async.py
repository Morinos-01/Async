import asyncio
from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    user_id: str
    items_total: float


async def check_stock(order: Order) -> bool:
    print(f"[stock] checking {order.order_id}")
    await asyncio.sleep(0.3)
    return True


async def get_delivery_price(order: Order) -> float:
    print(f"[delivery] pricing {order.order_id}")
    await asyncio.sleep(0.5)
    return 10.0


async def get_discount(order: Order) -> float:
    print(f"[discount] calculating {order.order_id}")
    await asyncio.sleep(0.2)
    return 5.0


async_tasks = [
    check_stock,
    get_delivery_price,
    get_discount
]


async def process_Order(order: Order) ->dict:
    result = {}
    tasks = []
    for task in async_tasks:
        coro = task(order)
        tasks.append(asyncio.create_task(coro))
    results = await asyncio.gather(*tasks)
    result['order_id'] = order.order_id
    result['in_stock'] = results[0]
    result['delivery_price'] = results[1]
    result['discount'] = results[2]
    result['final_price'] = order.items_total + result['delivery_price'] - result['discount'] 
    return result


async def main(orders: list):
    tasks = []
    for order in orders:
        task = asyncio.create_task(process_Order(order))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    order_1 = Order('123', '444', 45.0)
    order_2 = Order('5435', '8', 22.0)
    order_3 = Order('987089', '57964', 79.0)
    result = asyncio.run(main([order_1, order_2, order_3]))
    print('--------------')
    for i in result:
        print(i)
        print('---------------')