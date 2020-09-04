<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn flat type="a" href="/#/">
          <q-toolbar-title class="brand">
            <q-avatar>
              <!-- GitHub Org Avatar -->
              <img
                src="https://avatars0.githubusercontent.com/u/66812605?s=200&v=4"
              />
            </q-avatar>
            CGM One 整合服務管理頁面
          </q-toolbar-title>
        </q-btn>
        <q-space />
        <q-toggle
          v-model="$q.dark.mode"
          @input="toggleTheme()"
          unchecked-icon="wb_sunny"
          checked-icon="brightness_3"
          color="amber"
        />
      </q-toolbar>

      <q-tabs v-model="tab" align="left">
        <q-route-tab
          :name="getTabName(value.domain)"
          :to="'/' + getTabName(value.domain)"
          :label="key + ' ' + getTabName(value.domain)"
          v-for="(value, key) in hosts"
          :key="key"
        />
      </q-tabs>
    </q-header>

    <q-footer>
      <q-toolbar class="text-center">
        <q-space />
        <span>
          有任何問題設備或網路疑問請聯絡 CGM 網管
        </span>
        <q-space />
      </q-toolbar>
    </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import hosts from '../data/hosts';

export default {
  name: 'MainLayout',
  data() {
    return { hosts };
  },
  methods: {
    toggleTheme() {
      this.$q.dark.toggle();
      try {
        this.$q.sessionStorage.set('dark', this.$q.dark.isActive);
      } catch (e) {
        // data wasn't successfully saved due to
        // a Web Storage API error
      }
    },
    getTabName(domain) {
      if (domain === 'cgm.im') {
        return 'www';
      } else {
        return domain.split('.cgm.im')[0];
      }
    },
  },
  computed: {
    tab() {
      return this.$route.path.slice(1);
    },
  },
};
</script>

<style scoped>
.brand img {
  transform: rotate(0deg);
  transition: transform 1s ease-in-out;
}
.brand:hover img {
  transform: rotate(-720deg);
}
</style>
