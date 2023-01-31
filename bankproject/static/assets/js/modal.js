const distdatabox = document.getElementById('dist-data-box')
const distinput = document.getElementById('district')

const branchdatabox = document.getElementById('branch-data-box')
const branchinput = document.getElementById('branch')

const branchdefault = document.getElementById('branch-default')
$.ajax({
            type: 'GET',
            url: '/dist-json/',
            success: function(response){
                console.log(response.data)
                const distdata = response.data
                distdata.map(item=>{
                    const option =document.createElement('option')
                    option.textContent = item.name
                    option.setAttribute('value',item.id)
                    distdatabox.appendChild(option)
                })
            },
            error: function(error){
                console.log(error)
            }
      })

distinput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selecteddist = e.target.value


    branchdatabox.innerHTML=""
    const doption = document.createElement('option')
    doption.textContent = "choose your branch"
    branchdatabox.appendChild(doption)

    $.ajax({
        type:'GET',
        url:`branch-json/${selecteddist}/`,
        success:function(response){
            console.log(response.data)
            const branchdata = response.data
            branchdata.map(item=>{
                const option =document.createElement('option')
                option.textContent = item.name
                option.setAttribute('value',item.id)
                branchdatabox.appendChild(option)
            })
        },
        error:function(error){
            console.log(error)
        }
    })

    
})