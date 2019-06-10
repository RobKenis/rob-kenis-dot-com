<template>
  <v-container grid-list-xl>
    <v-layout v-bind="binding">
      <v-flex
        v-for="c in content.slice(0,maxSize)"
        :key="c.id"
        lg6
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
          title: "Jenkins Pipelines ♥ AWS",
          description: "Introduction to Jenkins",
          content: "How to setup Jenkins and leverage the pipelines plugin to create a CI/CD workflow to AWS Beanstalk.",
          link: "/posts/jenkins-pipelines-to-aws"
        },
        {
          id: "02",
          title: "Scaling your website to 1 million users",
          description: "Work in progress . . .",
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