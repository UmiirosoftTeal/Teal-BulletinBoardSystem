<template>
  <div id="app">
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <header>
      <h1>Teal BBS</h1>
      <p>Prott Ver</p>
    </header>
    <main>
      <h3>タイムライン</h3>
      <router-view />
    </main>
  </div>
</template>

<style>
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
}
header h1 {
  padding-left: 10px;
  font-size: 20px;
}
header p {
  padding-right: 10px;
  font-size: 12px;
}
main {
  max-width: 70ch;
  padding: 3em 1em;
  margin: auto;
  line-height: 1.75;
}
</style>