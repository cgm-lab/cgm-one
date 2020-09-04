<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  created() {
    this.$q.loading.show();
    this.fetchMetrics().then(() => this.$q.loading.hide());

    setInterval(() => {
      this.$q.loading.show();
      this.fetchMetrics().then(() => this.$q.loading.hide());
      console.log('Running');
    }, 60 * 5 * 1000);
  },
  methods: {
    async fetchMetrics() {
      let res = await fetch('https://one.cgm.im/api/metrics');
      let data = await res.json();
      this.$store.state.metrics = data;
    },
  },
};
</script>
<style>
@font-face {
  font-family: TaiwanPearl-Regular;
  src: url(https://cdn.jsdelivr.net/gh/max32002/TaiwanPearl@2.0/webfont/TaiwanPearl-Regular.woff2)
      format('woff2'),
    url(https://cdn.jsdelivr.net/gh/max32002/TaiwanPearl@2.0/webfont/TaiwanPearl-Regular.woff)
      format('woff');
}

body {
  font-family: TaiwanPearl-Regular, sans-serif, serif;
}
</style>
