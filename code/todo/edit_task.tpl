<p>编辑计划  ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>未完成</option>
    <option>已完成</option>
  </select>
  <br>
  <input type="submit" name="save" value="提交">
</form>
