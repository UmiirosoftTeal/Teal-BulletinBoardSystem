<template>
  <div class="home">
    <h3>タイムライン</h3>
    <for v-for="tweet in tweets" :key="tweet.id">
        <div class="card">
          <p class="username">{{ tweet.username }} id: {{ tweet.id }}</p>
          <p class="tweet">{{ tweet.tweet }}</p>
          <p class="postdate">{{ tweet.postdate }}</p>
        </div>
    </for>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tweets: [],
    };
  },
  mounted() {
    axios
      .get("https://teal-bbs.glitch.me/")
      .then((res) => {
        console.log(res);
        this.tweets = res.data;
      })
      .catch((err) => {
        this.tweets = err;
      });
  },
};
</script>

<style>
  .card {
    background: #5e746f;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 20px;
  }
  .username, .postdate {
    font-size: 14px;
    color: #9cb3af;
  }
</style>
