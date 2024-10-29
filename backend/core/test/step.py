from typing import Callable, Any, Dict

class TestStep:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    async def execute(self) -> Dict[str, Any]:
        try:
            value = await self.func()
            return {
                'status': 'PASS',
                'value': value
            }
        except Exception as e:
            return {
                'status': 'FAIL',
                'error': str(e)

            }