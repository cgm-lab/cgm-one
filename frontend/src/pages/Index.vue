<template>
  <q-page class="column">
    <h6 class="flex flex-center">Service</h6>
    <div class="flex flex-center q-gutter-md">
      <q-btn
        no-caps
        push
        v-for="(svc, i) in services"
        :key="i"
        :label="svc.name"
        :icon="svc.icon"
        color="accent"
        type="a"
        :href="svc.link"
        target="_blank"
        rel="noopener noreferrer"
      >
        <q-badge :color="svc.ok ? 'green' : 'red'" floating>
          <q-icon :name="svc.ok ? 'done' : 'error'" color="white" />
        </q-badge>
      </q-btn>
    </div>
  </q-page>
</template>

<script>
import services from '../data/services';

export default {
  name: 'PageIndex',
  data: () => ({
    services,
  }),
};
</script>
