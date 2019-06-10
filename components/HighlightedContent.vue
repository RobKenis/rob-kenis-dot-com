<template>
  <v-container grid-list-xl>
    <v-layout v-bind="binding">
      <v-flex
        v-for="c in content.slice(0,maxSize)"
        :key="c.id"
      >
        <FeaturedContent
          :title="c.title"
          :description="c.description"
          :content="c.content"
          :link="c.link"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import FeaturedContent from "~/components/FeaturedContent.vue";

export default Vue.extend({
  components: {
    FeaturedContent
  },
  props: {
    maxSize: {
      type: Number,
      default: 2
    },
    orientation: {
      type: String,
      default: "row"
    }
  },
  data: () => {
    return {
      content: [
        {
          id: "01",
          title: "First article",
          description: "First description",
          content: "First content",
          link: "https://robkenis.com/first-link"
        },
        {
          id: "02",
          title: "Second article",
          description: "Second description",
          content: "Second content"
        },
        {
          id: "03",
          title: "Third article",
          description: "Third description",
          content: "Third content",
          link: "https://robkenis.com/third-link"
        }
      ]
    };
  },
  computed: {
    binding() {
      const binding = {column: false, row: false};

      switch (this.orientation) {
        case "row":
          binding.row = true;
          break;
        case "column":
          binding.column = true;
          break;
      }

      return binding;
    }
  }
});
</script>