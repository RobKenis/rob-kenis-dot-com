<template>
  <v-container grid-list-xl>
    <v-layout
      v-bind="binding"
    >
      <v-flex>
        <featured-content
          title="Featured"
          link="/posts/jenkins-pipelines/"
          content="Something about Jenkins"
        />
      </v-flex>
      <v-flex>
        <featured-content
          title="Featured"
          link="/posts/jenkins-pipelines/"
          content="Something about Jenkins"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import FeaturedContent from "~/components/FeaturedContent.vue";

export default {
  components: {
    FeaturedContent
  },
  computed: {
    binding() {
      const binding = {}

      if (this.$vuetify.breakpoint.mdAndDown) {binding.column = true}

      return binding
    }
  }
};
</script>
