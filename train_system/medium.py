#Test script for the fine-grained train-ticketing microservice system
from locust import HttpUser, TaskSet, task, between, constant_pacing
import random

class StationServiceTask(TaskSet):
    @task
    def post_request(self):
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
        payload = {
            "id": "string",
            "name": name,
            "stayTime": 2
        }
        self.client.post("/api/v1/stationservice/stations", json=payload)

class PriceServiceTask(TaskSet):

    @task
    def get_request(self):
        self.client.get("/api/v1/priceservice/prices")

class TrainFoodServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/trainfoodservice/trainfoods")

class TrainServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/trainservice/trains")

class RouteServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/routeservice/routes")

class ContactsServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/contactservice/contacts")

class AdminBasicInfoServiceTask(TaskSet):

                @task
                def get_request(self):
                    self.client.get("/api/v1/adminbasicservice/adminbasic/contacts")

class AdminBasicInfoServiceTask2(TaskSet):

                @task
                def get_request(self):
                    self.client.get("/api/v1/adminbasicservice/adminbasic/stations")

class AdminBasicInfoServiceTask3(TaskSet):

                @task
                def get_request(self):
                    self.client.get("/api/v1/adminbasicservice/adminbasic/prices")

class AdminOrderServiceTask(TaskSet):

                @task
                def get_request(self):
                    self.client.get("/api/v1/adminorderservice/adminorder")

class BasicServiceTask(TaskSet):

        @task
        def get_request(self):
            cities = ["beijing", "shanghai", "xuzhou", "hangzhou"]
            city = random.choice(cities)
            self.client.get(f"/api/v1/basicservice/basic/{city}")

class OrderServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/orderservice/order")

class OrderService2Task(TaskSet):

        @task
        def get_request(self):
            orderIds = ["9bb0ac3e-b305-4929-84a9-2dfac9de3471", "a163e59c-ceec-4cc4-b6c0-6b113b9d2369", "c2a1cb69-0a94-4830-b7c9-987225f52942"]
            orderId = random.choice(orderIds)
            self.client.get(f"/api/v1/orderservice/order/{orderId}")

class OrderOtherServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/orderOtherService/orderOther")

class SeatServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/seatservice/welcome")


class StationFoodServiceTask(TaskSet):

        @task
        def get_request(self):
            cities = ["beijing", "shanghai", "nanjing", "hangzhou"]
            self.client.post("/api/v1/stationfoodservice/stationfoodstores", json=cities)

class Travel2ServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/travel2service/trips")

class UserServiceTask(TaskSet):

        @task
        def get_request(self):
            password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz123456', k=7))
            user = {
                 "documentNum": "2135488099312X",
                 "documentType": 1,
                 "email": "trainticket_notify@163.com",
                 "gender": 1,
                 "password": password,
                 "userId": "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                 "userName": "fdse_microservice"
            }
            self.client.put("/api/v1/userservice/users", json=user)

class AdminTravelServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/admintravelservice/admintravel")


class AdminRouteServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/adminrouteservice/adminroute")

class AdminUserServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/adminuserservice/users")

class AssuranceServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/assuranceservice/assurances")

class ConfigServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/configservice/configs")

class ConsignPriceServiceTask(TaskSet):

            @task
            def post_request(self):
                #randon generate beyondPrice, initialPrice
                initialPrice = random.randint(1, 10)
                beyondPrice = random.randint(1, 10)
                price = {
                          "beyondPrice": 1,
                          "id": "a1a942e5-032f-4b37-acb1-fcb8bd1657c2",
                          "index": 0,
                          "initialPrice": 2,
                          "initialWeight": 1,
                          "withinPrice": 2
                        }
                self.client.post("/api/v1/consignpriceservice/consignprice", json=price)

class ConsignServiceTask(TaskSet):

            @task
            def get_request(self):
                id = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
                self.client.get(f"/api/v1/consignservice/consigns/account/{id}")

class NotificationServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/notifyservice/test_send_mq")

class SecurityServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/securityservice/securityConfigs")

class TravelServiceTask(TaskSet):

            @task
            def get_request(self):
                tripId = "G1234"
                self.client.get("/api/v1/travelservice/train_types/{tripId}")

class CancelServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/cancelservice/welcome")

class ExeServiceTask(TaskSet):

        @task
        def get_request(self):
            self.client.get("/api/v1/executeservice/welcome")

class FoodDeliverServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/fooddeliveryservice/orders/all")

class FoodServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/foodservice/orders")

class InsidePaymentServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/inside_pay_service/inside_payment/account")

class OrderOther2ServiceTask(TaskSet):

            @task
            def get_request(self):
                travelDate = "2013-08-09"
                trainNumber = "1"
                self.client.get(f"/api/v1/orderOtherService/orderOther/{travelDate}/{trainNumber}")
class PaymentServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/paymentservice/payment")

class PreserveServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/preserveservice/welcome")

class RebookServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/rebookservice/welcome")
class waitorderServiceTask(TaskSet):

            @task
            def get_request(self):
                self.client.get("/api/v1/waitorderservice/orders")

class TravelPlanServiceTask(TaskSet):

            @task
            def post_request(self):
                data = {
                         "departureTime": "2013-08-12",
                         "endPlace": "shanghai",
                         "startPlace": "nanjing"
                       }
                self.client.post("/api/v1/travelplanservice/travelPlan/cheapest", json=data)
class RoutePlanServiceTask(TaskSet):

            @task
            def post_request(self):
                data = {
                         "endStation": "shanghai",
                         "num": 0,
                         "startStation": "nanjing",
                         "travelDate": "2013-08-01"
                       }
                self.client.post("/api/v1/routeplanservice/routePlan/cheapestRoute", json=data)

class PreserveOtherServiceTask(TaskSet):

                @task
                def get_request(self):
                    self.client.get("/api/v1/preserveotherservice/welcome")
# Station Service Test
class StationService(HttpUser):
    tasks = [StationServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12345"

# Price Service Test
class PriceService(HttpUser):
    tasks = [PriceServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16579"

# Train Food Service Test
class TrainFoodService(HttpUser):
    tasks = [TrainFoodServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:14567"

#  Train Service Test
class TrainService(HttpUser):
    tasks = [TrainServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:14567"

# Route Service Test
class RouteService(HttpUser):
    tasks = [RouteServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:11178"

# Contacts Service Test
class ContactsService(HttpUser):
    tasks = [ContactsServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12347"

# Admin Basic Info Service Test
class AdminBasicInfoService(HttpUser):
    tasks = [AdminBasicInfoServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18767"

# Admin Basic Info Service Test2
class AdminBasicInfoService2(HttpUser):
    tasks = [AdminBasicInfoServiceTask2]
    wait_time = constant_pacing(1)
    host = "http://localhost:18767"

# Admin Basic Info Service Test3
class AdminBasicInfoService3(HttpUser):
    tasks = [AdminBasicInfoServiceTask3]
    wait_time = constant_pacing(1)
    host = "http://localhost:18767"

# Admin Order Service Test
class AdminOrderService(HttpUser):
    tasks = [AdminOrderServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16113"

# Basic Service Test
class BasicService(HttpUser):
    tasks = [BasicServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:15680"

# Order Service Test
class OrderService(HttpUser):
    tasks = [OrderServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12031"

# Order Service Test2
class OrderService2(HttpUser):
    tasks = [OrderService2Task]
    wait_time = constant_pacing(1)
    host = "http://localhost:12031"

# Order Other Service Test
class OrderOtherService(HttpUser):
    tasks = [OrderOtherServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12032"

# Seat Service Test
class SeatService(HttpUser):
    tasks = [SeatServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18898"

# Station Food Service Test
class StationFoodService(HttpUser):
    tasks = [StationFoodServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12345"

# Travel2 Service Test
class Travel2Service(HttpUser):
    tasks = [Travel2ServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16346"

# User Service Test
class UserService(HttpUser):
    tasks = [UserServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12346"

#Admin Travel Service Test
class AdminTravelService(HttpUser):
    tasks = [AdminTravelServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:17525"

# Admin Route Service Test
class AdminRouteService(HttpUser):
    tasks = [AdminRouteServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16113"

# Admin User Service Test
class AdminUserService(HttpUser):
    tasks = [AdminUserServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18888"

# Assurance Service Test
class AssuranceService(HttpUser):
    tasks = [AssuranceServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18888"

# Config Service Test
class ConfigService(HttpUser):
    tasks = [ConfigServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:15679"

# Consign Price Service Test
class ConsignPriceService(HttpUser):
    tasks = [ConsignPriceServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:15679"

# Consign Service Test
class ConsignService(HttpUser):
    tasks = [ConsignServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12347"

# Notification Service Test
class NotificationService(HttpUser):
    tasks = [NotificationServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:17853"

# Security Service Test
class SecurityService(HttpUser):
    tasks = [SecurityServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18898"

# Travel Service Test
class TravelService(HttpUser):
    tasks = [TravelServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12346"

# Cancel Service Test
class CancelService(HttpUser):
    tasks = [CancelServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:15680"

# Execute Service Test
class ExecuteService(HttpUser):
    tasks = [ExeServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18957"

# Food Deliver Service Test
class FoodDeliverService(HttpUser):
    tasks = [FoodDeliverServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18957"

# Food Service Test
class FoodService(HttpUser):
    tasks = [FoodServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18856"

#InsidePaymentServiceTask Service Test
class InsidePaymentService(HttpUser):
    tasks = [InsidePaymentServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18673"

#OrderOther2ServiceTask Service Test
class OrderOther2Service(HttpUser):
    tasks = [OrderOther2ServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:12032"

#paymentservice Service Test
class PaymentService(HttpUser):
    tasks = [PaymentServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:17853"

#PreserveServiceTask Service Test
class PreserveService(HttpUser):
    tasks = [PreserveServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18856"

#rebool Service Test
class RebookService(HttpUser):
    tasks = [RebookServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16579"

#waitorderservice Service Test
class WaitOrderService(HttpUser):
    tasks = [waitorderServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:17525"

#Travel plan Service Test
class TravelPlanService(HttpUser):
    tasks = [TravelPlanServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:16346"

#RoutePlanServiceTask Service Test
class RoutePlanService(HttpUser):
    tasks = [RoutePlanServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:11178"

#PreserveOtherServiceTask
class PreserveOtherService(HttpUser):
    tasks = [PreserveOtherServiceTask]
    wait_time = constant_pacing(1)
    host = "http://localhost:18673"