<template>
  <div class="about">
    <h3>投稿</h3>
    <form :action=url method="POST" enctype="multipart/form-data" autocomplete="off">
      <input v-model="username" class="usernameInput" placeholder="ユーザー名を入力">
      <textarea v-model="tweet" class="tweetInput" rows="8" placeholder="投稿する文章を入力"></textarea>
      <input class="send" v-if="username && tweet" type="submit" v-on="post()" value="投稿する">
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      tweet: "",
      url: ""
    };
  },
  methods: {
    post() {
      this.url = "https://teal-bbs.glitch.me/post?username=" + this.username + "&tweet=" + this.tweet
     },
  },
};
</script>

<style>
  .usernameInput {
    width: 100%;
    padding: 10px;
  }
  .tweetInput {
    width: 100%;
    padding: 10px;
    resize: none;
  }
  .usernameInput, .tweetInput {
    font-size: 18px;
    border: none;
    margin-bottom: 10px;
    border-radius: 10px;
  }
  .usernameInput::placeholder, .tweetInput::placeholder {
    color:rgb(33, 33, 33);
    font-size: 15px;
  }
  .send {
    width: 100%;
    border: none;
    padding: 10px;
    border-radius: 10px;
    color: #fff;
    background-color: #7d9c95;
  }
</style>