<!-- eslint-disable -->
<template>
  <div id="app">

    <keep-alive>
      <b-tabs lazy>
        <b-tab 
          title="Section 1"
          :disabled=!isDisabled
        >
          <div class="p-3">
            <h1>Section 1</h1>
            <form>
            <div class="work-experiences">
              <div class="form-row" v-for="(experience, index) in workExperiences" :key="index">
                <div class="form-group col-md-6">
                  <label>Company</label>
                  <input v-model="experience.company" :name="`workExperiences[${index}][company]`" type="text" class="form-control" placeholder="Company">
                </div>
                <div class="form-group col-md-6">
                  <label>Title</label>
                  <input v-model="experience.title" :name="`workExperiences[${index}][title]`" type="text" class="form-control" placeholder="Title">
                </div>
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

            <b-button type="submit" variant="primary" @click="isDisabled = !isDisabled">Save and Continue</b-button>
          </div> 

        </b-tab>

        <b-tab 
          title="Section 2"
          :disabled=isDisabled
        >
          <div class="p-3">
            <h1>Section 2</h1>
            <b-button type="submit" variant="primary" v-on:click="isDisabled = !isDisabled">Back</b-button>
            <b-button type="submit" variant="primary" v-on:click="showAlert('Data submit')">Continue</b-button>
          </div>         
        </b-tab>

      </b-tabs>
    </keep-alive>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Questions',
  data() {
    return {
      isDisabled: true,
      workExperiences: [
        {
          company: "Foxconn",
          title: "Engineer"
        },
        {
          company: "Cherri Tech",
          title: "Software Engineer"
        }
      ],
    };
  },
  methods: {
      showAlert: (message) => {
        alert(message);
      }, 
      addExperience: () => {
        this.workExperiences.push({
          company: '',
          title: ''
        })
      },
    }
  };

</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
