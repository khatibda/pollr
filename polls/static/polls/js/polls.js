var DK = DK || {};

DK.Polls = DK.Polls || (function(){
	return {
		init: function(){
			$(".poll-delete").on('click',function(){
				return confirm("Are you sure you want to delete this poll?")
			});
		}
	}
})();

$(function() {
	DK.Polls.init();
});
