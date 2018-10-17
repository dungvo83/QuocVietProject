/*!
 Dung-TableData 1.0
 filter, pagination, maxRows.
 20181009
*/

//--------------------------------------------------------------- 
// pageLength: number of row in page
// pagination: 
// table:
// filter:
//---------------------------------------------------------------

function _tableData(table, filter, pagination, pageLength) {
            
    // var currentPage = parseInt(getURLParameter("page") == undefined? 1 : getURLParameter("page"));
    var maxRows = parseInt($(pageLength).val());
    console.log("maxRows: " + maxRows);
    var textFilter = "";
    tFilter();
    
    // max row change
    $(pageLength).on("change", function(){
        maxRows = $(this).val();
        tFilter();
    })

    // filter change
    $(filter).on('keyup', function(){
        textFilter = $(this).val().toLowerCase();
        tFilter();
    });

    function tFilter() {
        var total = 0;
        
        $(table + ' tbody tr').filter(function(){
            if( $(this).text().toLowerCase().indexOf(textFilter) > -1 ) {
                total++;
            }
        });

        tPagination(total);
    }

    function tPagination(total) {
        var maxPage = Math.ceil(total / maxRows);
        // previousPage = currentPage - 1;
        // nextPage = currentPage + 1;

        $(pagination).find("li").remove();

        // previous page
        $(pagination).append(
            '<li class="page-item"><a href="#" dt_idx="" class="page-link"><span aria-hidden="true">&laquo;</span></a></li>');
        // if(previousPage>0) {
        //     $(pagination).append(
        //         '<li class="page-item"><a href="#" dt_idx="" class="page-link"><span aria-hidden="true">&laquo;</span></a></li>');
        // } else {
        //     $(pagination).append(
        //         '<li class="page-item disabled"><a class="page-link"><span aria-hidden="true">&laquo;</span></a></li>');
        // }

        // set number page
        for(var i=0; i<maxPage; i++) {
            var page = i + 1;
            //...append
            $(pagination).append('<li class="page-item"><a class="page-link" href="#" dt_idx="'+page+'">'+page+'</a></li>');
        }

        // next page
        $(pagination).append(
            '<li class="page-item"><a href="#" dt_idx="" class="page-link"><span aria-hidden="true">&raquo;</span></a></li>');
        // if(nextPage<=numPages) {
        //     $(pagination).append(
        //         '<li class="page-item"><a href="?page='+ nextPage +'" class="page-link"><span aria-hidden="true">&raquo;</span></a></li>');
        // } else {
        //     $(pagination).append(
        //         '<li class="page-item disabled"><a class="page-link"><span aria-hidden="true">&raquo;</span></a></li>');
        // }


        $(pagination + " li a").on("click", function(){
            // var old_idx = $(pagination).find(".active").children().attr("dt_idx");
            
            var new_idx = $(this).attr("dt_idx");
            // setPageActive(new_idx, maxPage);
            // console.log("new_idx: ", new_idx);
            
            // if(new_idx <= 1) {
            //     $(pagination).find('li').eq(0).addClass('disabled');
            // }
            // if(new_idx>=numPages) {
            //     $(pagination).find('li').eq(numPages+1).addClass('disabled');
            // }

            // console.log("old_idx: " + old_idx);
            
            // display table
            tDisplay(new_idx, maxPage);
        })

        tDisplay(1, maxPage);

        // // set active current page
        // setPageActive(currentPage);
        // // calc row (from, to) showed
        // var start = (currentPage - 1)*maxRows;
        // var end = start + parseInt(maxRows);
        // // display table
        // tDisplay(start, end);
    }

    function tDisplay(index, maxPage) {

        // set page active
        // setPageActive(index);
        setPageActive(index, maxPage);

        // calc row (from, to) showed
        var start = (index - 1)*maxRows;
        var end = start + parseInt(maxRows);
        
        // count var
        var index = 0;

        // exec table
        $(table + " tbody tr").each(function() {
            if($(this).text().toLowerCase().indexOf(textFilter) > -1) {
                if(start <= index && index < end) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
                index++;
            } else {
                $(this).hide();
            }
        });
    }

    function setPageActive(index, maxPage){

        var index = parseInt(index);
        var maxPage = parseInt(maxPage);

        console.log("index: " + index + " - maxPage: " + maxPage);
        $(pagination + " li").removeClass("disabled");

        if(index <= 1) {
            $(pagination).find('li').eq(0).addClass('disabled');
        } else {
            // update dt_idx
            $(pagination).find('li').eq(0).children().attr("dt_idx",index-1);
        }

        if(index>=maxPage) {
            $(pagination).find('li').eq(maxPage+1).addClass('disabled');
        } else {
            // update dt_idx
            $(pagination).find('li').eq(maxPage+1).children().attr("dt_idx", index+1);
        }

        $(pagination + " li").removeClass('active');
        $(pagination).find('li').eq(index).addClass('active');

        console.log("pagination: " + $(pagination).html());
    }

    function getURLParameter(sParam) {
        var sPageURL = window.location.search.substring(1);
        var sURLVariables = sPageURL.split('&');
 
        for(var i=0; i<sURLVariables.length; i++){
            sParamName = sURLVariables[i].split('=');
            if(sParam==sParamName[0]) {
                return sParamName[1];
            }
        }
    }

}