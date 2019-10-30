<template>
    <div class="event-wrapper">
        
        <div class="table-body">
            
            <div class="body">
                <nuxt-link class="col" :to="'/users/' + id">  
                <div class="col">{{id}}</div>
                </nuxt-link>  
                <nuxt-link class="col" :to="'/users/' + first_name"> 
                <div class="col">{{first_name}}</div>
                </nuxt-link>  
                <div class="col">{{last_name}}</div>
                <div class="col">{{email}}</div>
                <div class="col">{{gender}}</div>
                <div class="col">{{age}}</div>
                
            </div>
            
        
        </div>
        
        
        
            
    </div>
</template>

<script>
export default {
    props: [
    "id",
    "index",
    "first_name",
    "last_name",
    "email",
    "gender",
    "age",  
  ],
    
}
</script>

<style lang="scss" scoped>
@import "@/styles/_mixins.scss";
.event-wrapper {
    .table-body {
        display: flex;
        flex-direction: column;
        background-color: $white;
        box-shadow: $box-shadow;
        padding: 10px 32px;
        margin-top: 8px;
        .col:first-child,
        .col:last-child {
            flex: 0.5;
            // color: $accent;
        }
        .body{
            display: flex;
            flex: 1;
            
            .col {
                display: flex;
                flex: 1;
                align-items: center;
                justify-content: center; 
                &.status{
                            color: #800020;
                            display: flex;
                            align-items: center;
                            justify-content: center; 
                            background-color: #F9E2E7;
                            border-radius: 99px;

                    }
                &.expand{
                    display: flex;
                    align-items: center;
                    justify-content: center; 
                    background-color: white;
                    color: black;
                }
            }

        }
        .sub-body{
            display: flex;
            flex: 1;
            padding: 10px 40px;
            margin-top: 8px;
            .col:first-child,
            .col:last-child {
                flex: 0.3;
                // color: $accent;
            }
            .col {
                display: flex;
                flex: 1;
                align-items: center;
                // justify-content: center; 
            
            }
        }
        .table-body-sub{
            display: flex;
            flex-direction: row;
            background-color: $white;
            box-shadow: $box-shadow;
            padding: 10px 32px;
            margin-top: 8px;
        }
        .line{
            margin-top: 8px;
            border: 0;
            border-top: 1px solid #ccc;
        }
    }
}
</style>