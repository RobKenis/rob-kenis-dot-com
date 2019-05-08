<template>
  <v-container>
    <v-layout
      align-center
      justify-center
    >
      <v-flex>
        <v-card>
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
            aspect-ratio="2.75"
          />

          <v-card-title
            primary-title
            height="100%"
          >
            <div>
              <h3 class="headline mb-0">
                {{ title }}
              </h3>
              <div>{{ description }}</div>
            </div>
          </v-card-title>

          <v-card-actions>
            <v-btn
              flat
              color="secondary"
              :disabled="link === undefined"
            >
              Open
            </v-btn>
            <v-spacer />
            <v-btn
              icon
              :disabled="content === undefined"
              @click="show = !show"
            >
              <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-slide-y-transition>
            <v-card-text v-show="show">
              {{ content }}
            </v-card-text>
          </v-slide-y-transition>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: {
    title: {
      type: String,
      default: "Highlight"
    },
    description: {
      type: String,
      default: "Description"
    },
    content: {
      type: String,
      default: undefined
    },
    link: {
      type: String,
      default: undefined
    }
  },
  data: () => ({
    show: false
  })
});
</script>
