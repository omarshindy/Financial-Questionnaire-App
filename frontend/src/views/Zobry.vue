<!-- eslint-disable -->
<template>
  <div id="app" class="container">
    <form>
      <h1>Work experiences</h1>

        <div class="form-row" v-for="(question, index) in questions" :key="index">
          <div class="form-group col-md-12">
            <label>Company</label>
            <input v-model="question.question" :name="`questions[${index}][question]`" type="text" class="form-control" placeholder="Company">
          </div>
    </div>

      <div class="form-group">
        <button @click="addExperience" type="button" class="btn btn-secondary">Add experience</button>
      </div>
      
      <hr>

      <div class="form-group">
        <button @click="submit" type="button" class="btn btn-primary">Submit</button>
      </div>

    </form>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "App",
  
  data: () => ({
    questions: [

    ]
  }),

  methods: {
    addExperience () {
      this.questions.push({
        question: '',
      })
    },

    submit () {
      const data = {
        workExperiences: this.workExperiences
      }
      alert(JSON.stringify(data, null, 2))
    }
  }
};
</script>

<style>
.work-experiences > div {
  margin: 20px 0;
  padding-bottom: 10px;
}
.work-experiences > div:not(:last-child) {
  border-bottom: 1px solid rgb(206, 212, 218);
}
</style>
