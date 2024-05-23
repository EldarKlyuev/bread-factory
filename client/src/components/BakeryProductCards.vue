<template>
  <div class="bakery-container">
    <h1>Хлебобулочный завод</h1>
    <h2>Продукция</h2>
    <div class="card-container">
      <div class="card" v-for="product in products" :key="product.id">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
      </div>
    </div>

    <h2>Заказы</h2>
    <div class="card-container">
      <div class="card" v-for="order in orders" :key="order.id">
        <h3>Заказ #{{ order.id }}</h3>
        <p>Клиент: {{ order.customer_name }}</p>
        <p>Дата: {{ order.date }}</p>
      </div>
    </div>

    <h2>Заказчики</h2>
    <div class="card-container">
      <div class="card" v-for="orderer in orderers" :key="orderer.id">
        <h3>{{ orderer.name }}</h3>
      </div>
    </div>

    <h2>Производственные цеха</h2>
    <div class="card-container">
      <div class="card" v-for="factor in factors" :key="factor.id">
        <h3>{{ factor.type_item }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: [],
      orders: [],
      factors: [],
      orderers: []
    };
  },
  mounted() {
    this.fetchProducts();
    this.fetchOrders();
    this.fetchOrderers();
    this.fetchFactors();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/item/');
        this.products = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных продукции:', error);
      }
    },
    async fetchOrders() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/order/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.orders = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных заказов:', error);
      }
    },
    async fetchOrderers() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/orderer/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.orderers = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных заказов:', error);
      }
    },
    async fetchFactors() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/factor/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        console.log(response.data)
        this.factors = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных заказов:', error);
      }
    }
  }
};
</script>

<style scoped>
.bakery-container {
  margin: 20px;
}

.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 10px;
}

.card {
  flex: 0 0 auto;
  width: 200px;
  margin: 10px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
