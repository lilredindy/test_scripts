create trigger hell_being_update_trg after update on hell_being
begin
  update hell_being set updatedon = datetime('NOW') where rowid = new.rowid;
end;

