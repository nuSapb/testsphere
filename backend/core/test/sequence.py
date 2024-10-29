from typing import List, Dict, Any
from dataclasses import dataclass, field

@dataclass
class TestSequence:
    name: str
    steps: List['TestStep'] = field(default_factory=list)
    results: Dict[str, Any] = field(default_factory=dict)

    def add_step(self, step: 'TestStep') -> None:
        self.steps.append(step)

    async def execute(self) -> Dict[str, Any]:
        results = {}
        for step in self.steps:
            try:
                result = await step.execute()
                results[step.name] = result
            except Exception as e:
                results[step.name] = {
                    'status': 'FAIL',
                    'error': str(e)
                }
                break
            return results
