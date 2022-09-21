"""
Module for performance test cases
"""

from locust import HttpUser, task


class PerformanceTests(HttpUser):
    """Test class for performance tests"""

    @task(1)
    def test_model_inference(self):
        """A method to test performance of model inference API"""
        res = self.client.post("/model_inference", json={"data": "test input"})
        print("res", res.json())
