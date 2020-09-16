<template>
  <div id="q-app" :class="loadClass">
    <Loading />
    <router-view />
  </div>
</template>
<script>
import Loading from './components/Loading';

export default {
  name: 'App',
  components: { Loading },
  data: () => ({ loadClass: '' }),
  created() {
    this.load();
    try {
      this.$q.dark.set(this.$q.localStorage.getItem('dark'));
    } catch (e) {
      // data wasn't successfully saved due to
      // a Web Storage API error
    }
    this.fetchMetrics().then(() => setTimeout(this.loaded, 1000));

    setInterval(() => {
      this.$q.loading.show();
      this.fetchMetrics().then(() => this.$q.loading.hide());
      console.log('Running');
    }, 60 * 5 * 1000);
  },
  methods: {
    load() {
      this.loadClass = '';
    },
    loaded() {
      this.loadClass = 'loaded';
    },
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
