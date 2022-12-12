<template>
  <div id="app">
    <header>
      <h1><a href="/">Teal BBS</a></h1>
      <p><router-link to="/new"><button class="createBtn">投稿を追加</button></router-link></p>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<style>
a {
  text-decoration: none;
  color: #bed8d1;
}
body,
html {
  padding: 0;
  margin: 0;
  background: #414a48;
  color: #ffffff;
  font-weight: bold;
}
header {
  color: #bed8d1;
  width: 100%;
  background: #414a48;
  border-bottom: solid 3px #5e746f;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
}
header h1 {
  padding-left: 15px;
  font-size: 20px;
}
header p {
  padding-right: 15px;
  font-size: 12px;
}
main {
  max-width: 70ch;
  padding: 3em 1em;
  margin: auto;
  line-height: 1.75;
}
.createBtn {
  border: none;
  background-color: #809b94;
  padding: 10px;
  color: #fff;
  border-radius: 20px;
}
</style>
