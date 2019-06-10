<template>
  <HighlightedContent :orientation="orientation" />
</template>

<script>
import HighlightedContent from "~/components/HighlightedContent.vue";

export default {
  components: {
    HighlightedContent
  },
  computed: {
    orientation() {
      if (this.$vuetify.breakpoint.mdAndDown) {
        return "column";
      }
      return "row";
    }
  }
};
</script>
