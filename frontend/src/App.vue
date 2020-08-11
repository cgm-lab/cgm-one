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
  },
  methods: {
    async fetchMetrics() {
      const res = await fetch('https://one.cgm.im/api/metrics');
      const data = await res.json();
      this.$store.state.metrics = data;
    },
  },
};
</script>
