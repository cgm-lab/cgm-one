<template>
  <q-page class="column q-pa-md">
    <h4 class="flex flex-center">Basic</h4>
    <div class="flex flex-center">
      <span class="text-subtitle1">Domain:</span>
      <q-chip outline color="accent" icon="dns" v-for="d in domains" :key="d">
        {{ d }}
      </q-chip>
    </div>
    <div class="flex flex-center" v-if="host.ip">
      <span class="text-subtitle1">IP:</span>
      <q-chip outline color="accent" icon="language">
        {{ host.ip }}
      </q-chip>
    </div>
    <div class="flex flex-center" v-if="!metric">
      Please install
      <q-btn
        flat
        color="primary"
        label="CGM One Client"
        type="a"
        href="https://github.com/cgm-lab/cgm-one-client/"
        target="_blank"
      />
      first.
    </div>
    <div v-if="metric">
      <div class="flex flex-center">
        <span class="text-subtitle1">OS:</span>
        <q-chip outline color="accent" icon="domain">
          {{ metric.os }}
        </q-chip>
      </div>
      <div class="flex flex-center" v-if="metric.lastUpdate">
        <span class="text-subtitle1">Last Update:</span>
        <q-chip outline color="accent" icon="access_time">
          {{ metric.lastUpdate }}
        </q-chip>
      </div>

      <h4 class="flex flex-center">Usage</h4>
      <!-- NETWORK -->
      <div class="row q-pa-md" v-if="metric.net">
        <div class="col-2">
          Network
        </div>
        <div class="col-10">
          <q-linear-progress
            stripe
            rounded
            size="25px"
            :value="metric.net.used / metric.net.total"
            :color="getColor(metric.net.used / metric.net.total)"
          >
            <div class="absolute-full flex flex-center">
              <q-badge
                color="white"
                text-color="accent"
                :label="
                  metric.net.used.toFixed(2) +
                    ' / ' +
                    metric.net.total.toFixed(2) +
                    ' ' +
                    metric.net.unit
                "
              />
            </div>
          </q-linear-progress>
        </div>
      </div>
      <!-- CPU -->
      <div class="row q-pa-md">
        <div class="col-2">
          CPU
        </div>
        <div class="col-10">
          <q-linear-progress
            stripe
            rounded
            size="25px"
            :value="metric.cpu.used / metric.cpu.total"
            :color="getColor(metric.cpu.used / metric.cpu.total)"
          >
            <div class="absolute-full flex flex-center">
              <q-badge
                color="white"
                text-color="accent"
                :label="
                  metric.cpu.used.toFixed(2) +
                    ' / ' +
                    metric.cpu.total.toFixed(2) +
                    ' ' +
                    metric.cpu.unit
                "
              />
            </div>
          </q-linear-progress>
        </div>
      </div>
      <!-- RAM -->
      <div class="row q-pa-md">
        <div class="col-2">
          RAM
        </div>
        <div class="col-10">
          <q-linear-progress
            stripe
            rounded
            size="25px"
            :value="metric.ram.used / metric.ram.total"
            :color="getColor(metric.ram.used / metric.ram.total)"
          >
            <div class="absolute-full flex flex-center">
              <q-badge
                color="white"
                text-color="accent"
                :label="
                  metric.ram.used.toFixed(2) +
                    ' / ' +
                    metric.ram.total.toFixed(2) +
                    ' ' +
                    metric.ram.unit
                "
              />
            </div>
          </q-linear-progress>
        </div>
      </div>
      <!-- VRAM -->
      <div
        class="row q-pa-md"
        v-for="(usage, title) in metric.vram"
        :key="title"
      >
        <div class="col-2" style="white-space: nowrap;">GPU {{ title }}</div>
        <div class="col-10">
          <q-linear-progress
            stripe
            rounded
            size="25px"
            :value="usage.used / usage.total"
            :color="getColor(usage.used / usage.total)"
          >
            <div class="absolute-full flex flex-center">
              <q-badge
                color="white"
                text-color="accent"
                :label="
                  usage.used.toFixed(2) +
                    ' / ' +
                    usage.total.toFixed(2) +
                    ' ' +
                    usage.unit +
                    ' (VRAM)'
                "
              />
            </div>
          </q-linear-progress>
        </div>
      </div>
      <!-- DISKS -->
      <div
        class="row q-pa-md"
        v-for="(usage, title) in metric.disks"
        :key="title"
      >
        <div class="col-2">Disk {{ title }}</div>
        <div class="col-10">
          <q-linear-progress
            stripe
            rounded
            size="25px"
            :value="usage.used / usage.total"
            :color="getColor(usage.used / usage.total)"
          >
            <div class="absolute-full flex flex-center">
              <q-badge
                color="white"
                text-color="accent"
                :label="
                  usage.used.toFixed(2) +
                    ' / ' +
                    usage.total.toFixed(2) +
                    ' ' +
                    usage.unit
                "
              />
            </div>
          </q-linear-progress>
        </div>
      </div>
    </div>

    <h4 class="flex flex-center desktop-only" v-if="monitor">Monitor</h4>
    <div class="flex flex-center desktop-only" v-if="monitor">
      <iframe
        :src="monitor"
        style="min-width: 80%; min-height: 800px;"
      ></iframe>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Dashboard',
  props: { name: String, host: Object, monitor: String },
  data: () => ({}),
  methods: {
    getColor(value) {
      if (value <= 0.7) return 'positive';
      if (value <= 0.9) return 'warning';
      return 'negative';
    },
  },
  computed: {
    domains() {
      let domains = [];
      if (this.host.domain === 'cgm.im') {
        return ['cgm.cs.ntust.edu.tw', this.host.domain];
      }
      return [this.name + '.cgm.im', this.host.domain];
    },
    metric() {
      return (
        this.$store.state.metrics[this.host.local] ||
        this.$store.state.metrics[this.host.ip] ||
        null
      );
    },
  },
};
</script>
