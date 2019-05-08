<template>
  <v-app dark>
    <v-toolbar>
      <v-avatar
        size="2em"
        color="white"
      >
        <img
          src="/v.png"
          alt="avatar"
        >
      </v-avatar>
      <v-toolbar-title>Rob Kenis</v-toolbar-title>
      <v-spacer />
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          flat
        >
          {{ link.title }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer height="auto">
      <v-layout
        justify-center
        row
        wrap
      >
        <v-flex
          lighten-2
          py-3
          text-xs-center
          white--text
          xs12
        >
          &copy;2019 —
          <strong>Rob Kenis</strong>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      links: [
        {url: "https://github.com/RobKenis", title: "GitHub"},
        {url: "https://www.linkedin.com/in/robkenis", title: "LinkedIn"},
        {url: "https://twitter.com/robkenis", title: "Twitter"}
      ]
    };
  }
};
</script>
