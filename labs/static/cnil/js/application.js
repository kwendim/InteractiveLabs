window.onload = function() {

  var go_to_next_task = function() {
      var current_task = $("#task-progress-text .current_task");
      var current_task_int = parseInt(current_task.text(), 10);
      var next_task_int = current_task_int + 1;
      var max = parseInt($("#task-progress").attr("data-tasks"), 10) - 1;
      if (next_task_int <= max && next_task_int >= 1) {
          toggle_task_count(next_task_int, max);
          go_to_task(current_task, current_task_int, next_task_int);
      } else {
          finish_lab()
      }
      return false
  };
  var finish_lab = function(e) {
    document.location.href="./"
  };
  var toggle_task_count = function(current_task, max) {
    if(current_task==0 || current_task==max){
      var task_progress = $("#task-progress");
      task_progress.addClass("hidden");;
    } else {
      var task_progress = $("#task-progress");
      task_progress.removeClass("hidden");;
    }
  };
  var go_to_previous_task = function(e) {
      var current_task = $("#task-progress-text .current_task");
      var current_task_int = parseInt(current_task.text(), 10);
      var next_task_int = current_task_int - 1;
      var max = parseInt($("#task-progress").attr("data-tasks"), 10) - 1;
      if (next_task_int <= max && next_task_int >= 1) {
          toggle_task_count(next_task_int, max);
          go_to_task(current_task, current_task_int, next_task_int)
      }
      return false
  };
  var go_to_task = function(current_task_span, current_task_int, next_task_int) {
      var task = $("#task-" + current_task_int);
      task.addClass("hidden");
      var next_task = $("#task-" + next_task_int);
      next_task.removeClass("hidden");
      current_task_span.text(next_task_int);
  };

  $(".next").click(go_to_next_task);

  if (!window.jQuery) {
      // jQuery is not loaded
      alert("jQuery not loaded");
  }
}
