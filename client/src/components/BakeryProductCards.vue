<template>
  <div class="bakery-container">
    <div class="background-image"></div>
    <div class="user-info">
      <img :src="user.logo" alt="User Logo" class="user-logo"/>
      <span class="user-name">{{ user.name }}</span>
    </div>
    <h1>Хлебобулочный завод</h1>
    <h2>Изделия</h2>
    <div class="card-container">
      <div class="card" v-for="item in items" :key="item.id">
        <button class="delete-button" @click="deleteItem(item.id)">×</button>
        <h3>Код изделия: {{ item.id }}</h3>
        <h3>Название: {{ item.name }}</h3>
        <h3>Вес изделия: {{ item.weight }}</h3>
      </div>
    </div>

    <h2>Заказы</h2>
    <div class="card-container">
      <div class="card" v-for="order in orders" :key="order.id">
        <button class="delete-button" @click="deleteOrder(order.id)">×</button>
        <h3>Заказ #{{ order.id }}</h3>
        <p>Дата: {{ order.date }}</p>
      </div>
    </div>

    <h2>Заказчики</h2>
    <div class="card-container">
      <div class="card" v-for="orderer in orderers" :key="orderer.id">
        <button class="delete-button" @click="deleteOrderer(orderer.id)">×</button>
        <h3>{{ orderer.name }}</h3>
      </div>
    </div>

    <h2>Производственные цеха</h2>
    <div class="card-container">
      <div class="card" v-for="factor in factors" :key="factor.id">
        <button class="delete-button" @click="deleteFactor(factor.id)">×</button>
        <h3>Тип изделий: {{ factor.type_item }}</h3>
        <p>Сорт муки: {{ factor.sort_muka }}</p>
      </div>
    </div>

    <h2>Продукция</h2>
    <div class="card-container">
      <div class="card" v-for="production in productions" :key="production.id">
        <button class="delete-button" @click="deleteProduction(production.id)">×</button>
        <h3>Код продукции: {{ production.code_items }}</h3>
        <p>Готовность продукции: {{ production.is_ready ? 'готов' : 'не готов' }}</p>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
      orders: [],
      factors: [],
      orderers: [],
      productions: [],
      user: {
        name: 'Эльдар', // Здесь можно задать имя пользователя
        logo: 'src/assets/Account-User-PNG-Photo.png' // Здесь можно задать ссылку на логотип пользователя
      }
    };
  },
  mounted() {
    this.fetchProducts();
    this.fetchOrders();
    this.fetchOrderers();
    this.fetchFactors();
    this.fetchProduction();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/item/');
        this.items = response.data;
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
        console.error('Ошибка при загрузке данных заказчиков:', error);
      }
    },
    async fetchFactors() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/factor/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.factors = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных производственных цехов:', error);
      }
    },
    async fetchProduction() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/production/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.productions = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке данных продукции:', error);
      }
    },
    async deleteItem(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/item/${id}/`);
        this.items = this.items.filter(item => item.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении изделия:', error);
      }
    },
    async deleteOrder(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/order/${id}/`);
        this.orders = this.orders.filter(order => order.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении заказа:', error);
      }
    },
    async deleteOrderer(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/orderer/${id}/`);
        this.orderers = this.orderers.filter(orderer => orderer.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении заказчика:', error);
      }
    },
    async deleteFactor(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/factor/${id}/`);
        this.factors = this.factors.filter(factor => factor.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении производственного цеха:', error);
      }
    },
    async deleteProduction(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/production/${id}/`);
        this.productions = this.productions.filter(production => production.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении продукции:', error);
      }
    }
  }
};

</script>

<style scoped>
.bakery-container {
  margin: 20px;
  position: relative;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('src/assets/bulochki.jpg'); /* Замените на реальную ссылку */
  background-size: cover;
  background-position: center;
  filter: blur(10px);
  z-index: -1;
}

.user-info {
  position: absolute;
  top: 10px;
  left: 90%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  z-index: 1;
}

.user-logo {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

.user-name {
  font-weight: bold;
  font-size: 1.2em;
}

.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 10px;
}

.card {
  position: relative;
  flex: 0 0 auto;
  width: 200px;
  margin: 10px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: rgba(255, 255, 255, 0.8); /* Полупрозрачный фон для лучшей читаемости */
  z-index: 0;
}

.delete-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: red;
  color: white;
  border: none;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  cursor: pointer;
  z-index: 1;
}

.delete-button:hover {
  background-color: darkred;
}
</style>
