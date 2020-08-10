import hosts from '../data/hosts';

const tabs = [];

for (let [name, h] of Object.entries(hosts)) {
  let path;
  if (h.domain === 'cgm.im') {
    path = 'www';
  } else {
    path = h.domain.split('.cgm.im')[0];
  }
  tabs.push({
    path,
    component: () => import('pages/Dashboard.vue'),
    props: { name, host: h },
  });
}

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      ...tabs,
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
