<template>
  <v-layout
    column
    justify-center
    align-center
  >
    <v-flex
      xs12
      sm8
      md6
    >
      <Highlight title="Blogs" />
    </v-flex>
  </v-layout>
</template>

<script>
import Highlight from '~/components/Highlight.vue';

export default {
  components: {
    Highlight
  }
}
</script>
