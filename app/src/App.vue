<template>
  <v-app dark>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Rob</span>
        <span class="font-weight-light">
          Kenis
        </span>
      </v-toolbar-title>
      <v-spacer />
      <v-btn
        flat
        href="https://github.com/RobKenis/rob-kenis-dot-com"
        target="_blank"
      >
        <span class="mr-2">
          Github
        </span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <LandingPage />
    </v-content>
  </v-app>
</template>

<script>
import LandingPage from "./components/LandingPage";

export default {
  name: 'App',
  components: {
    LandingPage,
  },
  data () {
    return {
      //
    }
  }
}
</script>
